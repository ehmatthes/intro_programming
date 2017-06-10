{%- extends 'basic.tpl' -%}
{% from 'mathjax.tpl' import mathjax %}


{%- block header -%}
  {% include "resources/my_templates/intro_python_header.html" %}
{%- endblock header -%}


{%- block input -%}
  {%- set marker_tags=[] -%}
  {%- set line_count=[] -%}

{# Pick out the lines that need highlighting, and set style appropriately. #}
{%- for line in super().split('\n') -%}

{# Look for beginning and end of actual lines of code. #}
{%- if '<pre>' in line -%}
{%- set _ = marker_tags.append('<pre>') -%}
{%- elif '</pre>' in line -%}
{%- set _ = marker_tags.append('</pre>') -%}
{%- endif -%}

{# Highlight any lines in cell metadata highlight_lines. #}
{%- if '<pre>' in marker_tags and '</pre>' not in marker_tags -%}
{%- set _ = line_count.append(1) -%}
{# use a {}.get() here, to deal with missing metadata #}
{%- if line_count|length in cell.metadata.get('highlight_lines',None)|expand_highlight_lines -%}
{%- if line_count|length > 1 -%}
<div class="highlighted_code_line">{{ line }}</div>
{%- else -%}
{# Need to treat the placement of highlighted line different for first line. #}
{{ line|replace('<pre>', '<pre><div class="highlighted_code_line">') }}</div>
{%- endif -%}
{%- else -%}
{{ line }}
{% endif -%}

{%- else -%}
{{ line }}
{%- endif -%}

{%- endfor -%}

{%- endblock input -%}


{# Need a unique identifier for each output cell, to toggle individual cells' visbility.
    Make an empty list, and add to the list each time an output block is rendered.
    Use the length of the list as the unique identifier.
    #}
{% set cell_count=[] %}

{% block output %} {# outputs works, but hidden by output #}
  <div class='text-right'>
    <button id='show_output_{{ cell_count|length }}' class='btn btn-success btn-xs show_output' target='{{ cell_count|length }}'>show output</button>
    <button id='hide_output_{{ cell_count|length }}' class='btn btn-success btn-xs hide_output' target='{{ cell_count|length }}'>hide output</button>
  </div>
  {{ super() }}
  {% set _ = cell_count.append(1) %}
{% endblock output %}

{# Will these blocks (output, stream_stdout) always match 1:1?
    If there's a stream_stdout block, it's inside an output block,
    so we should be able to use the cell_count, maybe -1 to match value before increment?
   Can't use indentation in this next block, because output uses <pre> tag, which will
    keep the whitespace from template indentation.
   Also applying this to stream_stderr because some blocks focus on errors.
	#}
{% block stream_stdout %}
{% for line in super().split('\n') %}
{% if '<div class="output_subarea output_stream output_stdout output_text">' in line %}
<div id="output_subarea_{{ cell_count|length }}" class="output_subarea output_stream output_stdout output_text">
{%- else -%}
{{ line }}
{%- endif -%}
{% endfor %}
{% endblock stream_stdout %}



{# Show/ hide png output. #}
{% block display_data %}
{% for line in super().split('\n') %}
{{ line|replace('<div class="output_png output_subarea ">', '<div id="output_subarea_' ~ cell_count|length ~ '" class="output_png output_subarea ">') }}

{% endfor %}
{% endblock display_data %}



{% block error %}
{% for line in super().split('\n') %}
{% if '<div class="output_subarea output_text output_error">' in line %}
<div id="output_subarea_{{ cell_count|length }}" class="output_subarea output_text output_error">
{%- else -%}
{{ line }}
{%- endif -%}
{% endfor %}
{% endblock error %}


{% block markdowncell %}
{{ super()|replace('<code>', '<code class="inline_code">') }}
{% endblock markdowncell %}


{# Body block is defined by intro_python_index, or intro_python_default. #}


{% block footer %}
  {% include "resources/my_templates/include_jquery.html" %}
  </html>
{% endblock footer %}