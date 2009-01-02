from viewbase import ViewBase
from metadata import FieldsMetadata
from widgetselector import RecordViewWidgetSelector
from widgets import RecordViewWidget

class RecordViewBase(ViewBase):
    """This class allows you to credate a table widget.

    :Modifiers:

    see modifiers in :mod:`sprox.viewbase`

    Here is an example listing of the first user in the test database.

    >>> from sprox.test.base import Town, setup_database, setup_records, User
    >>> session, engine, metadata = setup_database()
    >>> user = setup_records(session)
    >>> class UserRecordView(RecordViewBase):
    ...     __model__ = User
    ...     __omit_fields__ = ['created']
    >>> user_view = UserRecordView(session)
    >>> from sprox.fillerbase import RecordFiller
    >>> class UserRecordFiller(RecordFiller):
    ...     __model__ = User
    >>> user_filler = UserRecordFiller(session)
    >>> value = user_filler.get_value({'user_id':1})
    >>> print user_view(value=value)
    <table xmlns="http://www.w3.org/1999/xhtml" class="recordviewwidget">
    <tr><th>Name</th><th>Value</th></tr>
    <tr class="recordfieldwidget">
        <td>
            <b>_password</b>
        </td>
        <td>
        </td>
    </tr>
    <tr class="recordfieldwidget">
        <td>
            <b>user_id</b>
        </td>
        <td> 1
        </td>
    </tr>
    <tr class="recordfieldwidget">
        <td>
            <b>user_name</b>
        </td>
        <td> asdf
        </td>
    </tr>
    <tr class="recordfieldwidget">
        <td>
            <b>email_address</b>
        </td>
        <td> asdf@asdf.com
        </td>
    </tr>
    <tr class="recordfieldwidget">
        <td>
            <b>display_name</b>
        </td>
        <td>
        </td>
    </tr>
    <tr class="recordfieldwidget">
        <td>
            <b>town_id</b>
        </td>
        <td> 1
        </td>
    </tr>
    <tr class="recordfieldwidget">
        <td>
            <b>town</b>
        </td>
        <td> 1
        </td>
    </tr>
    <tr class="recordfieldwidget">
        <td>
            <b>password</b>
        </td>
        <td>
        </td>
    </tr>
    <tr class="recordfieldwidget">
        <td>
            <b>groups</b>
        </td>
        <td> 5
        </td>
    </tr>
    </table>
    >>> session.rollback()
    """


    __metadata_type__         = FieldsMetadata
    __widget_selector_type__  = RecordViewWidgetSelector
    __base_widget_type__      = RecordViewWidget

    def _do_get_field_widget_args(self, field_name, field):
        """Override this method do define how this class gets the field
        widget arguemnts
        """
        args = super(RecordViewBase, self)._do_get_field_widget_args( field_name, field)
        args['field_name'] = field_name
        if self.__provider__.is_relation(self.__entity__, field_name):
            args['entity'] = self.__entity__
            args['field_name'] = field_name
        return args