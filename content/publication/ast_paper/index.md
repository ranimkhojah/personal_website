---
title: 'Evaluating the Trade-offs of Diversity-Based Test Prioritization: An Experiment'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - admin
  - Francisco Gomes de Oliveira Neto
  - Chi Hong (Nigel) Chao


date: '2023-04-16T00:00:00Z'
doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: '2023-04-16T00:00:00Z'

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# Publication name and optional abbreviated publication name.
publication: In *AST Conference*

abstract: Different test prioritization techniques detect faults at earlier stages of test execution. To this end, Diversity-based techniques (DBT) have been cost-effective by prioritizing the most dissimilar test cases to maintain effectiveness and coverage with lower resources at different stages of the software development life cycle, called levels of testing (LoT). Diversity is measured on static test specifications to convey how different test cases are from one another. However, there is little research on DBT applied to semantic similarities of words within tests. Moreover, diversity has been extensively studied within individual LoT (unit, integration and system), but the trade-offs of such techniques across different levels are not well understood. This paper aims to reveal relationships between DBT and the LoT, as well as to compare and evaluate the cost-effectiveness and coverage of different diversity measures, namely Jaccard’s Index, Levenshtein, Normalized Compression Distance (NCD), and Semantic Similarity (SS). We perform an experiment on the test suites of 7 open source projects on the unit level, 1 industrial project on the integration level, and 4 industry projects on the system level (where one project is used on both system and integration levels). Our results show that SS increases test coverage for system-level tests, and the differences in failure detection rate of each diversity increase as more prioritised tests execute. In terms of execution time, we report that Jaccard is the fastest, whereas Levenshtein is the slowest and, in some cases, simply infeasible to run. In contrast, Levenshtein detects more failures on integration level, and Jaccard more on system level. 

# Summary. An optional shortened abstract.

tags: [Diversity-based testing, Test Case Prioritization, Natural Language Processing (NLP), Level of Testing (LoT)]

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

# url_pdf: '/ast.pdf'
url_code: 'https://github.com/ranimkhojah/test-prioritization-tools'

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
<!-- 
{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

{{% callout note %}}
Create your slides in Markdown - click the _Slides_ button to check out the example.
{{% /callout %}}

Supplementary notes can be added here, including [code, math, and images](https://wowchemy.com/docs/writing-markdown-latex/). -->
