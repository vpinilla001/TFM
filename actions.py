# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

# This is a simple example for a custom action which utters "Hello World!"
from rasa_sdk import Action
from rasa_sdk.events import SlotSet, UserUttered
# from typing import Any, Text, Dict, List
# from rasa_sdk.executor import CollectingDispatcher

import string
import random
import pandas as pd

from functions_bot import plot_serie, plot_serie2
from functions_bot import plot_hist, plot_hist2
from functions_bot import describe_information, describe_information2


class DefaultFallback(Action):
    def name(self):
        return "my_fallback_action"

    def run(self, dispatcher, tracker, domain):
        response = "Mmmm, no estoy seguro de lo que quieres decirme..." + "\n" + "Me puedes preguntar sobre  \n ● Gráfica de una señal \n  ● Información de una señal \n ● Análisis estadístico de una señal"
        dispatcher.utter_message(text=response)


class ActionGrapichHist(Action):
    def name(self):
        return "action_grafica_hist"

    def run(self, dispatcher, tracker, domain):
        N = 20
        name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))

        id = tracker.get_slot("senal").upper()
        fecha = tracker.get_slot("fecha")
        color = tracker.get_slot("color_value")

        if fecha[0] != None and fecha[1] != None:
            plot_hist(id, fecha[0], fecha[1] + ' ' + "23:59:59" , name, color)
        else:
            plot_hist2(id, name, color)

        path = "http://localhost:7000/img/" + name + '.png'
        dispatcher.utter_message(text="Aquí tiene su gráfica", image=path)
        result = [SlotSet("senal", None), SlotSet("fecha", None),
                  SlotSet("color_value", None), SlotSet("tipo_grafica", None)]

        return result


class ActionGrapichSerie(Action):
    def name(self):
        return "action_grafica_serie"

    def run(self, dispatcher, tracker, domain):
        N = 20
        name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))

        id = tracker.get_slot("senal").upper()
        fecha = tracker.get_slot("fecha")
        mark = tracker.get_slot("mark_value")

        if fecha[0] != None and fecha[1] != None:
            plot_serie(id, fecha[0], fecha[1] + ' ' + "23:59:59", name, mark)
        else:
            plot_serie2(id, name, mark)

        path = "http://localhost:7000/img/" + name + '.png'
        dispatcher.utter_message(text="Aquí tiene su gráfica", image=path)
        result = [SlotSet("senal", None), SlotSet("fecha", None),
                  SlotSet("mark_value", None), SlotSet("tipo_grafica", None)]

        return result


class ActionInformation(Action):
    def name(self):
        return "action_informacion"

    def run(self, dispatcher, tracker, domain):
        id = tracker.get_slot("senal").upper()
        descripcion = tracker.get_slot("descripcion")
        unidad = tracker.get_slot("unidad")
        tipo = tracker.get_slot("tipo")

        data = pd.read_csv('datasets/cic_descripcion.csv', engine='python', delimiter=';', index_col=0)

        response = "La señal " + id
        if descripcion != None and unidad == None and tipo == None:
            descripcion_text = data[descripcion].loc[id]
            response = response + " hace referencia a  " + descripcion_text
        elif descripcion == None and unidad != None and tipo == None:
            unidad_text = data[unidad].loc[id]
            response = response + " tiene como unidades " + unidad_text
        elif descripcion == None and unidad == None and tipo != None:
            tipo_text = data[tipo].loc[id]
            response = response + " es del tipo " + tipo_text
        elif descripcion != None and unidad != None and tipo == None:
            descripcion_text = data[descripcion].loc[id]
            unidad_text = data[unidad].loc[id]
            response = response + " hace referencia a  " + descripcion_text + " y tiene como unidades " + unidad_text
        elif descripcion != None and unidad == None and tipo != None:
            descripcion_text = data[descripcion].loc[id]
            tipo_text = data[tipo].loc[id]
            response =  response + " hace referencia a  " + descripcion_text + " y es del tipo " + tipo_text
        elif descripcion == None and unidad != None and tipo != None:
            unidad_text = data[unidad].loc[id]
            tipo_text = data[tipo].loc[id]
            response = response + " tiene como unidades " + unidad_text + " y es del tipo " + tipo_text
        else:
            descripcion_text = data['descripcion'].loc[id]
            unidad_text = data['unidad'].loc[id]
            tipo_text = data['tipo'].loc[id]
            response = response + " hace referencia a  " + descripcion_text + ", tiene como unidades " + unidad_text + " y es del tipo " + tipo_text

        dispatcher.utter_message(text=response)
        result = [SlotSet("senal", None), SlotSet("descripcion", None), SlotSet("unidad", None), SlotSet("tipo", None)]

        return result


class ActionDescribe(Action):
    def name(self):
        return "action_descripcion"

    def run(self, dispatcher, tracker, domain):
        id = tracker.get_slot("senal").upper()
        fecha = tracker.get_slot("fecha")

        if fecha[0] != None and fecha[0] != None:
            inf = describe_information(id, fecha[0], fecha[1] + ' ' + "23:59:59")
        else:
            inf = describe_information2(id)

        n_obs = inf[0]; media = inf[1]; desv = inf[2]; min_ = inf[3]
        p_25 = inf[4]; p_50 = inf[5]; p_75 = inf[6]; max_ = inf[7]
        response = "El análisis descriptivo de la señal {0} es el siguiente:".format(id) + "\n" + "Nº de observaciones: {0} \n Media: {1} \n Desviación: {2} \n Valor mínimo: {3} \n Percentil 25%: {4} \n Percentil 50%: {5} \n Percentil 75%: {6} \n Valor máximo: {7} \n ".format(n_obs, media, desv, min_, p_25, p_50, p_75, max_)
        dispatcher.utter_message(text = response)
        result = [SlotSet("senal", None), SlotSet("fecha", None)]

        return result

