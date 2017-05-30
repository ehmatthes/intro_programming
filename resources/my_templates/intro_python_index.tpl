{%- extends 'resources/my_templates/intro_python_base.tpl' -%}

{% block body %}
  <body>
    {% include "resources/my_templates/navbar.html" %}
      <div class="container" id="notebook-container">

        {{ super() }}

      </div>
  </body>
{%- endblock body %}
