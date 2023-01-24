from os import makedirs
import datetime

def data_save(folder, file_format, wrire_mode, data):
    try:
        makedirs('Результаты')
    except:
        pass
    finally:
        date = datetime.datetime.utcnow().strftime('%d-%m-%Y %H.%M.%S')
        print(date)
        try:
            makedirs(f'Результаты/{folder}')
        except:
            pass

        with open('Результаты/' + folder + '/' + date + '.' + file_format,
                  wrire_mode,
                  encoding='windows-1251') as file:
            file.write(data)

    return None