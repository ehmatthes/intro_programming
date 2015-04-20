{%- block header -%}
	 {% include "intro_python_header.html" %}
{%- endblock header -%}

{% block body %}
<body>
  {% include "navbar.html" %}
  {% include "index_body.html" %}
</body>
{%- endblock body %}

{% block footer %}
{% include "include_jquery.html" %}
</html>
{% endblock footer %}

