# {{ name }}

{{ summary }}

{% for stat in stats %}- {{ stat }}
{% endfor %}

## Experience

{% for job in experience %}

**{{ job.title }}**, *{{ job.location }}*

  {% for desc in job.description %}
  - {{ desc }}
  {% endfor %}

{% endfor %}

## Education

{% for edu in education %}
- **{{ edu.degree }}*, *{{ edu.location }}*
{% endfor %}
