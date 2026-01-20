---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: about.biography
    id: about
    content:
      title: Biography
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: admin
  - block: collection
    id: recent
    content:
      title: Selected Publications
      text: |-
        {{% callout note %}}
        See [all publications](./publication/).
        {{% /callout %}}

      filters:
        folders:
          - publication
        exclude_featured: false
        featured_only: true
    design:
      columns: '2'
      view: 2
  - block: markdown
    id: talks
    content:
      title: Talks & Presentations
      text: |-
        **Chatbots in Software Engineering**
        *Scientific highlights at the WASP Winter Conference (ca 500 attendees)*, Örebro, Sweden (2026)

        **Understanding and Evaluating Chatbots in Software Engineering**
        *Licentiate Seminar*, Chalmers University of Technology, Gothenburg, Sweden (2025)

        **The Art of Using ChatGPT**
        *Innovation Fika (ca 300 attendees)*, Volvo Trucks, Gothenburg, Sweden (2024)

        **ChatGPT Usage in Software Engineering Practice**
        *Invited Talk*, SystemWeaver, Gothenburg, Sweden (2024)

        **Programming without a Programming Language**
        *Workshop*, Iceberry, Gothenburg, Sweden (2024)

        **Chatbots in Software Engineering**
        *Invited Talk*, RISE Research Institutes of Sweden, Borås, Sweden (2024)

        **From Human-to-Human to Human-to-Bot Interactions in Software Engineering**
        *Paper presentation*, AIware (Co-located with FSE), Porto de Galinhas, Brazil (2024)

        **Beyond Code Generation: An Observational Study of ChatGPT Usage in Software Engineering Practice**
        *Paper presentation*, FSE, Porto de Galinhas, Brazil (2024)

        **Evaluating the Trade-offs of Text-based Diversity in Test Prioritisation**
        *Paper presentation*, AST (co-located with ICSE), Melbourne, Australia (2023)

        **Evaluating N-best Calibration of Natural Language Understanding for Dialogue Systems**
        *Paper presentation*, SigDIAL, Edinburgh, Scotland (2022)
    design:
      columns: '2'
  - block: portfolio
    id: projects
    content:
      title: Projects
      filters:
        folders:
          - project
      # Default filter index (e.g. 0 corresponds to the first `filter_button` instance below).
      default_button_index: 0
      # Filter toolbar (optional).
      # Add or remove as many filters (`filter_button` instances) as you like.
      # To show all items, set `tag` to "*".
      # To filter by a specific tag, set `tag` to an existing tag name.
      # To remove the toolbar, delete the entire `filter_button` block.
      buttons:
        - name: All
          tag: '*'
        - name: Dialogue Systems
          tag: dial
        - name: Software Development
          tag: soft

    design:
      # Choose how many columns the section has. Valid values: '1' or '2'.
      columns: '1'
      view: masonry
      flip_alt_rows: false
  - block: markdown
    id: service
    content:
      title: Academic Service
      text: |-
        <div style="font-size: 0.9rem;">

        **Committee Member:**

        • Program committee member - BotSE Workshop (co-located with ICSE 2024)

        • Publicity Chair - AIware Conference (co-located with ASE 2025)

        • Program committee member - BoatSE Workshop (co-located with ICSE 2025)

        **Student Volunteer:**

        • ICSE 2023 - Melbourne, Australia

        • ICSE 2024 - Lisbon, Portugal

        • ASE 2025 - Seoul, South Korea

        **Teaching duties:**

        • Data Management (2025-2026): Teaching, Assignment design, assessment.

        • Fundamentals of Programming (2024-2025): Teaching, Creating course material.

        • Object Oriented Programming (2018-2020, 2022-2023): Teaching, Creating course material, assessment.

        • Distributed Systems (2024): Supervising and assessing project groups.

        **Thesis Supervision:**

        • *Bachelor thesis:* "Developer Behavior in Response to LLM-Generated Code Refactoring Suggestions", Main supervisor (2025) - with David Schön, Faiza Amjad, and Tehreem Asif.

        • *Master thesis:* "Leveraging Large Language Models for Cybersecurity Risk Assessment", Co-supervisor (2024) - with Fikret Mert Gültekin and Oscar Lilja

        </div>
    design:
      columns: '2'
  - block: experience
    id: experience
    content:
      title: Experience
      # Date format for experience
      #   Refer to https://wowchemy.com/docs/customization/#date-format
      date_format: Jan 2006
      # Experiences.
      #   Add/remove as many `experience` items below as you like.
      #   Required fields are `title`, `company`, and `date_start`.
      #   Leave `date_end` empty if it's your current employer.
      #   Begin multi-line descriptions with YAML's `|2-` multi-line prefix.
      items:
        - title: Researcher (PhD student)
          company: Chalmers University of Technology
          company_logo: org-gc
          location: Gothenburg
          date_start: '2022-12-01'
          date_end: ''
          description: PhD project (Chatbots in Software Engineering) funded by Wallenberg AI, Autonomous Systems and Software Program (WASP).
        - title: Software Developer
          company: Volvo Trucks Technology
          company_logo: org-v
          location: Gothenburg
          date_start: '2022-09-01'
          date_end: '2022-11-01'
          description: Automated the translation process followed in infotainment systems.
        - title: Teaching Assistant
          company: Chalmers University of Technology
          company_logo: org-gc
          location: Gothenburg
          date_start: '2022-06-01'
          date_end: '2022-08-30'
          description: |2-
            Patricipated in Girls Code Club (GCC); a coding camp that welcomes gymnasium students and women who are looking to pursue a career within software engineering and computer science.
        - title: Research Assistant
          company: Chalmers University of Technology
          company_logo: org-gc
          location: Gothenburg
          date_start: '2021-01-01'
          date_end: '2022-06-30'
          description: |2-
              Assistance with research related to FaaS applications.
              Performing data processing and analysis using NLP techniques.
        - title: Teaching Assistant
          company: University of Gothenburg
          company_logo: org-x
          location: Gothenburg
          date_start: '2018-09-01'
          date_end: '2022-11-30'
          description: |2-
              Courses - Discrete Mathematics, Object-oriented Programming, Mobile and Web Development.

    design:
      columns: '2'
  # - block: accomplishments
  #   content:
  #     # Note: `&shy;` is used to add a 'soft' hyphen in a long heading.
  #     title: 'Accomplish&shy;ments'
  #     subtitle:
  #     # Date format: https://wowchemy.com/docs/customization/#date-format
  #     date_format: Jan 2006
  #     # Accomplishments.
  #     #   Add/remove as many `item` blocks below as you like.
  #     #   `title`, `organization`, and `date_start` are the required parameters.
  #     #   Leave other parameters empty if not required.
  #     #   Begin multi-line descriptions with YAML's `|2-` multi-line prefix.
  #     items:
  #       - certificate_url: https://www.coursera.org
  #         date_end: ''
  #         date_start: '2021-01-25'
  #         description: ''
  #         organization: Coursera
  #         organization_url: https://www.coursera.org
  #         title: Neural Networks and Deep Learning
  #         url: ''
  #       - certificate_url: https://www.edx.org
  #         date_end: ''
  #         date_start: '2021-01-01'
  #         description: Formulated informed blockchain models, hypotheses, and use cases.
  #         organization: edX
  #         organization_url: https://www.edx.org
  #         title: Blockchain Fundamentals
  #         url: https://www.edx.org/professional-certificate/uc-berkeleyx-blockchain-fundamentals
  #       - certificate_url: https://www.datacamp.com
  #         date_end: '2020-12-21'
  #         date_start: '2020-07-01'
  #         description: ''
  #         organization: DataCamp
  #         organization_url: https://www.datacamp.com
  #         title: 'Object-Oriented Programming in R'
  #         url: ''
  #   design:
  #     columns: '2'
  # - block: collection
  #   id: posts
  #   content:
  #     title: Recent Posts
  #     subtitle: ''
  #     text: ''
  #     # Choose how many pages you would like to display (0 = all pages)
  #     count: 5
  #     # Filter on criteria
  #     filters:
  #       folders:
  #         - post
  #       author: ""
  #       category: ""
  #       tag: ""
  #       exclude_featured: false
  #       exclude_future: false
  #       exclude_past: false
  #       publication_type: ""
  #     # Choose how many pages you would like to offset by
  #     offset: 0
  #     # Page order: descending (desc) or ascending (asc) date.
  #     order: desc
  #   design:
  #     # Choose a layout view
  #     view: compact
  #     columns: '2'
  # - block: markdown
  #   content:
  #     title: Gallery
  #     subtitle: ''
  #     text: |-
  #       {{< gallery album="demo" >}}
  #   design:
  #     columns: '1'
  # - block: collection
  #   id: featured
  #   content:
  #     title: Featured Publications
  #     filters:
  #       folders:
  #         - publication
  #       featured_only: true
  #   design:
  #     columns: '2'
  #     view: card
  
  # - block: collection
  #   id: talks
  #   content:
  #     title: Service and Talks
  #     filters:
  #       folders:
  #         - event
  #   design:
  #     columns: '2'
  #     view: compact
  # - block: tag_cloud
  #   content:
  #     title: Popular Topics
  #   design:
  #     columns: '2'


---
