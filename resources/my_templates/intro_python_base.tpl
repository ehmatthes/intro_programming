{%- extends 'basic.tpl' -%}
{% from 'mathjax.tpl' import mathjax %}


{%- block header -%}
  {% include "resources/my_templates/intro_python_header.html" %}
{%- endblock header -%}

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

{% block footer %}
  {% include "resources/my_templates/include_jquery.html" %}
  </html>
{% endblock footer %}