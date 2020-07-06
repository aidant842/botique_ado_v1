from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _ #using as _ is effectively assigning an alias to the gettext_lazy so we can call it as _() instead of gettext_lazy()


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'products/custom_widget_templates/custom_clearable_file_input.html'
