import view
import model
import text


def start():
    while True:
        select = view.menu()
        match select:
            case 1:
                if model.open_file():
                    view.print_message(text.load_successful)
                else:
                    view.print_message(text.error_load)
            # case 2:
            #     if model.save_file():
            #         view.print_message(text.save_successful)
            #     else:
            #         view.print_message(text.error_save)
            case 2:
                index_start = view.input_start_date()
                index_end = view.input_end_date()
                view.show_notes_filter(model.animals_reestr, index_start, index_end)
            case 3:
                view.show_notes(model.animals_reestr, text.empty_reestr)
            case 4:
                index = view.input_show_note_id()
                view.show_note(model.animals_reestr, index)
            case 5:
                model.open_file()
                new = view.add_note()
                model.add_note(new)
                view.print_message(text.add_successful(new.get('name')))
                model.save_file()
                view.print_message(text.save_successful)
                model.open_file()
            case 6:
                word = view.search_word()
                result = model.search(word)
                view.show_notes(result, text.empty_search(word))
            case 7:
                index = view.input_change_id()
                new = view.change_note()
                result = model.change_note(index, new)
                if result:
                    view.print_message(text.change_successful(result))
                    model.save_file()
                    view.print_message(text.save_successful)
                    model.open_file()
                else:
                    view.print_message(text.error_changed)
            case 8:
                index = view.input_del_id()
                result = model.remove_note(index)
                if result:
                    view.print_message(text.del_successful(result))
                    model.save_file()
                    view.print_message(text.save_successful)
                    model.open_file()
                else:
                    view.print_message(text.error_deleted)
            case 9:
                view.print_message(text.exit_message)
                break
