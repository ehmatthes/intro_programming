{%- block header -%}
	 {% include "intro_python_header.html" %}
{%- endblock header -%}

{% block body %}
<body>
  {% include "navbar.html" %}
    <div class="container" id="notebook-container">
    </div>
</body>
{%- endblock body %}

{% block footer %}
{% include "include_jquery.html" %}
</html>
{% endblock footer %}

