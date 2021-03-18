require('./app.css');
import 'select2';

jquery(document).ready(function() {
    jquery(".mailselect").select2({
        tags: true,
        tokenSeparators: [',', ' ']
    })
});
