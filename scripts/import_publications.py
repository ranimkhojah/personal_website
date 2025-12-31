#!/usr/bin/env python3
"""
Import publications from BibTeX to Hugo Academic format
"""

import os
import re
from pathlib import Path
import bibtexparser
from bibtexparser.bparser import BibTexParser
from datetime import datetime


def main():
    """Main import function"""
    # Paths
    project_root = Path(__file__).parent.parent
    bib_file = project_root / "publications.bib"
    pub_dir = project_root / "content" / "publication"

    if not bib_file.exists():
        print(f"Error: {bib_file} not found", flush=True)
        return

    # Parse BibTeX file
    print(f"Parsing {bib_file}...", flush=True)
    with open(bib_file, 'r', encoding='utf-8') as f:
        parser = BibTexParser(common_strings=True)
        bib_database = bibtexparser.load(f, parser)

    print(f"Found {len(bib_database.entries)} publication(s)", flush=True)

    # Generate Hugo markdown for each publication
    for entry in bib_database.entries:
        generate_publication(entry, pub_dir)

    print(f"Successfully imported {len(bib_database.entries)} publication(s)!", flush=True)


def generate_publication(entry, pub_dir):
    """Generate Hugo markdown file for a publication"""
    # Create slug from citation key
    slug = entry.get('ID', '').lower().replace('_', '-')

    # Create publication folder
    pub_folder = pub_dir / slug
    pub_folder.mkdir(parents=True, exist_ok=True)

    # Extract fields
    title = entry.get('title', '').replace('{', '').replace('}', '')
    authors = parse_authors(entry.get('author', ''))
    year = entry.get('year', '')
    month = entry.get('month', '1')
    abstract = entry.get('abstract', '')
    keywords = entry.get('keywords', '')

    # Parse tags and featured flag
    tags, featured = parse_keywords(keywords)

    # Determine publication type
    pub_type = get_publication_type(entry.get('ENTRYTYPE', ''))

    # Get publication venue
    venue = entry.get('booktitle', entry.get('journal', ''))

    # Get URLs
    url_pdf = entry.get('pdf', '')
    url_code = entry.get('url', '')

    # Build date
    try:
        month_num = int(month) if month.isdigit() else 1
        date_str = f"{year}-{month_num:02d}-01T00:00:00Z"
    except:
        date_str = f"{year}-01-01T00:00:00Z"

    # Generate frontmatter
    frontmatter = generate_frontmatter(
        title=title,
        authors=authors,
        date=date_str,
        pub_type=pub_type,
        venue=venue,
        abstract=abstract,
        tags=tags,
        featured=featured,
        url_pdf=url_pdf,
        url_code=url_code,
        year=year
    )

    # Write index.md
    index_file = pub_folder / "index.md"
    index_file.write_text(frontmatter, encoding='utf-8')

    # Generate cite.bib
    cite_bib = generate_cite_bib(entry)
    cite_file = pub_folder / "cite.bib"
    cite_file.write_text(cite_bib, encoding='utf-8')

    print(f"  Generated {slug}", flush=True)


def parse_authors(author_string):
    """Parse author string and return list of author names"""
    if not author_string:
        return ['admin']

    # Split by 'and'
    authors = [a.strip() for a in author_string.split(' and ')]

    # Convert to list format
    author_list = []
    for author in authors:
        # Check if it's the main author (Khojah, Ranim)
        if 'Khojah' in author:
            author_list.append('admin')
        else:
            # Convert "Last, First" to "First Last"
            parts = [p.strip() for p in author.split(',')]
            if len(parts) == 2:
                author_list.append(f"{parts[1]} {parts[0]}")
            else:
                author_list.append(author)

    return author_list if author_list else ['admin']


def parse_keywords(keyword_string):
    """Parse keywords and extract tags and featured flag"""
    if not keyword_string:
        return [], False

    # Split by comma
    keywords = [k.strip() for k in keyword_string.split(',')]

    # Check for featured
    featured = 'featured' in [k.lower() for k in keywords]

    # Filter out 'featured' from tags
    tags = [k for k in keywords if k.lower() != 'featured']

    return tags, featured


def get_publication_type(entry_type):
    """Map BibTeX entry type to Hugo publication type"""
    type_map = {
        'article': '2',
        'inproceedings': '1',
        'conference': '1',
        'book': '5',
        'phdthesis': '7',
        'mastersthesis': '7',
        'techreport': '4',
        'unpublished': '3',
    }
    return type_map.get(entry_type.lower(), '0')


def generate_frontmatter(title, authors, date, pub_type, venue, abstract, tags, featured, url_pdf, url_code, year):
    """Generate Hugo frontmatter"""
    frontmatter = f"""---
title: '{title}'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
"""

    for author in authors:
        frontmatter += f"  - {author}\n"

    frontmatter += f"""

date: '{date}'
doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: '{date}'

# Show date in publication list
show_date: false

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['{pub_type}']

# Publication name and optional abbreviated publication name.
publication: ''

abstract: {abstract}

# Summary. An optional shortened abstract.
summary: "*{venue}*, {year}"

tags: {tags}

# Display this page in the Featured widget?
featured: {str(featured).lower()}

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

"""

    if url_pdf:
        frontmatter += f"url_pdf: '{url_pdf}'\n"
    if url_code:
        frontmatter += f"url_code: '{url_code}'\n"

    frontmatter += """
# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# image:
#   caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/pLCdAaMFLTE)'
#   focal_point: ''
#   preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
# projects:
#   - example

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
# slides: example
---
"""

    return frontmatter


def generate_cite_bib(entry):
    """Generate cite.bib content from BibTeX entry"""
    entry_type = entry.get('ENTRYTYPE', 'article')
    cite_key = entry.get('ID', 'publication')
    title = entry.get('title', '')
    author = entry.get('author', '')
    year = entry.get('year', '')

    cite = f"@{entry_type}{{{cite_key},\n"
    cite += f"  title={{{title}}},\n"
    cite += f"  author={{{author}}},\n"
    cite += f"  year={{{year}}}"

    # Add optional fields
    if 'booktitle' in entry:
        cite += f",\n  booktitle={{{entry['booktitle']}}}"
    if 'journal' in entry:
        cite += f",\n  journal={{{entry['journal']}}}"
    if 'volume' in entry:
        cite += f",\n  volume={{{entry['volume']}}}"
    if 'number' in entry:
        cite += f",\n  number={{{entry['number']}}}"
    if 'pages' in entry:
        cite += f",\n  pages={{{entry['pages']}}}"
    if 'publisher' in entry:
        cite += f",\n  publisher={{{entry['publisher']}}}"

    cite += "\n}\n"

    return cite


if __name__ == "__main__":
    main()
