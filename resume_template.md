# {{ name }}

{{ summary }}

📄 {{ stats.total }} refereed publications, {{stats.citations}} citations.

⚙️ {{ technical_stack }}

## Experience

{% for job in experience %}

**{{ job.title }}**, *{{ job.location }}*

  {% for desc in job.description %}
  - {{ desc }}
  {% endfor %}

{% endfor %}

## Education

{% for edu in education %}
- **{{ edu.degree }}**, *{{ edu.location }}*
{% endfor %}
