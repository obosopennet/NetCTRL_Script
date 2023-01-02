from jinja2 import Template

def render_template(template_name, **kwargs):
    """
    Render a Jinja2 template file.
    """
    with open(f"templates/{template_name}") as f:
        template_str = f.read()

    template = Template(template_str)
    config_str = template.render(**kwargs)

    return config_str
