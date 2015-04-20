{%- extends 'basic.tpl' -%}
{% from 'mathjax.tpl' import mathjax %}


{%- block header -%}
	 {% include "my_templates/intro_python_header.html" %}
{%- endblock header -%}

{% block body %}
<body>
  {% include "my_templates/navbar.html" %}
    <div class="container" id="notebook-container">
{{ super() }}
    </div>
</body>
{%- endblock body %}

{% block footer %}
{% include "my_templates/include_jquery.html" %}
</html>
{% endblock footer %}