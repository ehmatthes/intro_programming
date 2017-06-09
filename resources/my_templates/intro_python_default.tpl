{%- extends 'resources/my_templates/intro_python_base.tpl' -%}

{% block body %}
  <body>
    {% include "resources/my_templates/navbar.html" %}
      <div class="container" id="notebook-container">
        <div class='text-right'>
          <button id='show_output_all' class='btn btn-success btn-xs show_output_all'>Show all output</button>
          <button id='hide_output_all' class='btn btn-success btn-xs hide_output_all'>Hide all output</button>
        </div>

        {{ super() }}

      </div>
  </body>
{%- endblock body %}