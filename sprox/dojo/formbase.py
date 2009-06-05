"""
fillerbase Module

Classes to help fill widgets with data

Copyright (c) 2008 Christopher Perkins
Original Version by Christopher Perkins 2008
Released under MIT license.
"""

from sprox.formbase import FormBase, EditableForm, AddRecordForm
from sprox.widgetselector import SAWidgetSelector
from sprox.widgets.dojo import SproxDojoSelectShuttleField, SproxDojoSortedSelectShuttleField

class DojoSAWidgetSelector(SAWidgetSelector):
    """Dojo-Specific Widget Selector"""
    default_multiple_select_field_widget_type = SproxDojoSelectShuttleField

class DojoFormBase(FormBase):
    """FormBase for Dojo

    see :class:`sprox.formbase.FormBase`
    
    """
    __widget_selector_type__ = DojoSAWidgetSelector
    
class DojoEditableForm(EditableForm):
    """Creates a form for editing records that has select shuttles for the multiple relations.
    
    :Modifiers:
      see :class:`sprox.formbase.FormBase`

    :Usage:
    
    >>> from sprox.dojo.formbase import DojoEditableForm
    >>> from formencode import Schema
    >>> from formencode.validators import FieldsMatch
    >>> class Form(DojoEditableForm):
    ...     __model__ = User
    ...     __limit_fields__       = ['user_name', 'groups']
    >>> edit_form = Form()
    >>> print edit_form() # doctest: +XML
    <form action="" method="post" class="required tableform">
        <div>
                <input type="hidden" id="sprox_id" class="hiddenfield" name="sprox_id" value="" />
                <input xmlns="http://www.w3.org/1999/xhtml"
           xmlns:py="http://genshi.edgewall.org/"
           type="hidden" name="_method" class="sproxmethodputhiddenfield" id="_method"
           value="PUT"
           py:attrs="attrs" />
        </div>
        <table border="0" cellspacing="0" cellpadding="2" >
            <tr class="even" id="user_name.container" title="" >
                <td class="labelcol">
                    <label id="user_name.label" for="user_name" class="fieldlabel">User Name</label>
                </td>
                <td class="fieldcol" >
                    <input type="text" id="user_name" class="textfield" name="user_name" value="" />
                </td>
            </tr>
            <tr class="odd" id=".container" title="" >
                <td class="labelcol">
                    <label id=".label" for="" class="fieldlabel">Groups</label>
                </td>
                <td class="fieldcol" >
                    <div xmlns="http://www.w3.org/1999/xhtml" dojoType="twdojo.SelectShuttle" id="groups_SelectShuttle">
        <div style="float:left; padding: 5px; width:10em;">
            Available<br />
            <select class="shuttle" id="groups_src" multiple="multiple" name="" size="5">
                    <option value="1">0</option><option value="2">1</option><option value="3">2</option><option value="4">3</option><option value="5">4</option>
            </select>
        </div>
        <div style="float:left; padding: 25px 5px 5px 0px;" id="groups_Buttons">
            <button class="shuttle" id="groups_AllRightButton">&gt;&gt;</button><br />
            <button class="shuttle" id="groups_RightButton">&gt;</button><br />
            <button class="shuttle" id="groups_LeftButton">&lt;</button><br />
            <button class="shuttle" id="groups_AllLeftButton">&lt;&lt;</button>
        </div>
        <div style="float:left; padding: 5px; width:10em;">
                Selected<br />
                <select class="shuttle" id="groups" multiple="multiple" name="groups" size="5">
                </select>
        </div>
        <script type="text/javascript">
        //create an object of this type here
        </script>
    </div>
                </td>
            </tr>
            <tr class="even" id="submit.container" title="" >
                <td class="labelcol">
                    <label id="submit.label" for="submit" class="fieldlabel"></label>
                </td>
                <td class="fieldcol" >
                    <input type="submit" class="submitbutton" value="Submit" />
                </td>
            </tr>
        </table>
    </form>
"""
    __widget_selector_type__ = DojoSAWidgetSelector