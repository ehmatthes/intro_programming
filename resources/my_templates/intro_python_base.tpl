{%- extends 'basic.tpl' -%}
{% from 'mathjax.tpl' import mathjax %}


{%- block header -%}
  {% include "resources/my_templates/intro_python_header.html" %}
{%- endblock header -%}

{% block body %}
  <body>
   {% include "resources/my_templates/navbar.html" %}
      <div class="container" id="notebook-container">
        {{ super() }}
      </div>
  </body>
{%- endblock body %}

{% block footer %}
  {% include "resources/my_templates/include_jquery.html" %}
  </html>
{% endblock footer %}