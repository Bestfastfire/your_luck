# pip install pysimplegui
import PySimpleGUI as sg
import luck as lc


def btn(txt='', size=2):
    return sg.Button(size=(size, 1), button_text=txt)


def get_value(m_list, sequence) -> int:
    i = 0

    for k, v in m_list.items():
        if v == True:
            if i == sequence:
                return int(k) - 10 if int(k) > 9 else int(k)

            else:
                i += 1

    return -1


def in_line(value):
    return value[0]


def row_person(person):
    return [
        sg.Text(text=person[0], size=(17, 2), background_color='grey', justification='center'),
        sg.Text(text=person[1], size=(17, 2), background_color='grey', justification='center'),
        sg.Text(text=person[2], size=(17, 2), background_color='grey', justification='center')
    ]


def get_layout(num, persons):
    return [
               [sg.Text(text='Digite seu nome e escolha 2 números nas linhas abaixo:', size=(50, 0))],
               [
                   sg.InputText(size=(50, 5), key='txt'),
                   sg.Button(button_text='Salvar', size=(7, 1))
               ],
               [sg.Radio(text, 1, default=True) for text in num],
               [sg.Radio(text, 2, default=True) for text in num],
               [sg.Text(text='')],
               [sg.Text(text='Lista de Participantes:')]
           ] + [row_person(person) for person in ([['Nome', 'Nº 1', 'Nº 2']] + persons)] \
           + [
               [sg.Text(text='')],
               [sg.Button(button_text='Sortear', size=(12, 1), pad=(175, 0))]
           ]


class LayoutLuck:
    def __init__(self):
        self.num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.lc = lc.Luck()
        self.layout = get_layout(self.num, self.lc.persons)
        self.window = sg.Window("Teste de Sorte").layout(self.layout)

    def show(self):
        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED:
                break

            elif event == 'Sortear':
                values = self.lc.generate()
                winners = values[1]

                sg.Popup(f"Os números sorteados foram {values[0][0]} e {values[0][1]}, e "
                         + ("não teve ganhadores!" if len(winners) < 1 else
                            ("os ganhadores foram: " + ', '.join(map(lambda v: v[0], winners)))),
                         title='Resultado')

            elif event == 'Salvar':
                name = str(values['txt']).strip()

                if name == '':
                    sg.Popup('Por favor, preencha os campos corretamente!', title='Erro')

                else:
                    n1 = get_value(values, 0)
                    n2 = get_value(values, 1)

                    self.lc.put_person(name, n1, n2)
                    nWindow = sg.Window('Teste de Sorte') \
                        .layout(get_layout(self.num, self.lc.persons))

                    self.window.close()
                    self.window = nWindow


screen = LayoutLuck()
screen.show()
