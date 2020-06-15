## test 1
* saludo
   - utter_saludo
* informacion{"unidad":"unidad","senal":"CIC0004"}
    - slot{"senal":"CIC0004"}
    - slot{"unidad":"unidad"}
    - action_informacion
    - slot{"senal":null}
    - slot{"descripcion":null}
    - slot{"unidad":null}
    - slot{"tipo":null}
* agradecer
   - utter_agradecer
* grafica_hist{"fecha":"2018-02-14", "tipo_grafica":"histograma"}
   - slot{"fecha":["2017-01-28", "2018-02-14"]}
   - slot{"tipo_grafica":"histograma"}
   - utter_ask_senal
* dar_senal{"senal":"CIC0002"}
    - slot{"senal":"CIC0002"}
    - utter_ask_tipo_hist
* color{"color_value":"verde"}
    - slot{"color_value":"verce"}
    - action_grafica_hist
    - slot{"senal":null}
    - slot{"fecha":null}
    - slot{"fecha":null}
    - slot{"color_value":null}
    - slot{"tipo_grafica":null}
* buen_humor
   - utter_buen_humor
* despedida
   - utter_ask_feedback
* feedback{"feedback_value":"negativo"}
   - slot{"feedback_value":"negativo"}
   - utter_feedback_neg
   - utter_despedida
* grafica{"fecha":"2018-04-12"}
   - slot{"fecha":["2017-07-11", "2018-04-12"]}
   - utter_ask_senal
* grafica{"senal":"cic0001"}
   - slot{"senal": "cic0001"}
   - utter_ask_tipo_grafica
* grafica_serie{"tipo_grafica":"serie"}
   - slot{"tipo_grafica":"serie"}
   - utter_ask_tipo_serie
* mark{"mark_value": "si"}
    - slot{"mark_value": "si"}
    - action_grafica_serie
    - slot{"senal": null}
    - slot{"fecha": null}
    - slot{"fecha": null}
    - slot{"mark_value": null}
    - slot{"tipo_grafica": null}
* descripcion{"fecha": "2018-07-16"}
    - slot{"fecha": ["2016-11-20", "2018-07-16"]}
    - utter_ask_senal
* dar_senal{"senal":"cic0003"}
    - slot{"senal":"cic0003"}
    - action_descripcion
    - slot{"senal": null}
    - slot{"fecha": null}


## test 2
* saludo
   - utter_saludo
* descripcion
    - utter_ask_senal
* dar_senal{"senal":"cic0007"}
    - slot{"senal":"cic0007"}
    - action_descripcion
    - slot{"senal": null}
    - slot{"fecha": null}
* grafica_serie{"tipo_grafica":"serie"}
    - slot{"tipo_grafica":"serie"}
    - utter_ask_senal
* dar_senal{"senal":"CIC0006"}
    - slot{"senal":"CIC0006"}
    - utter_ask_tipo_serie
* mark{"mark_value":"no"}
    - slot{"mark_value":"no"}
    - action_grafica_serie
    - slot{"senal":null}
    - slot{"fecha":null}
    - slot{"fecha":null}
    - slot{"mark_value":null}
    - slot{"tipo_grafica":null}
* agradecer
   - utter_agradecer
* informacion
    - utter_ask_senal
* dar_senal{"senal": "CIC0008"}
    - slot{"senal": "CIC0008"}
    - action_informacion
    - slot{"senal": null}
    - slot{"descripcion": null}
    - slot{"unidad": null}
    - slot{"tipo": null}
* buen_humor
   - utter_buen_humor
* despedida
   - utter_ask_feedback
* feedback{"feedback_value":"positivo"}
   - slot{"feedback_value":"positivo"}
   - utter_feedback_pos
   - utter_despedida
* grafica{"senal":"cic0005"}
   - slot{"senal": "cic0005"}
   - utter_ask_tipo_grafica
* grafica_hist{"tipo_grafica":"histograma"}
   - slot{"tipo_grafica":"histograma"}
   - utter_ask_tipo_hist
* color{"color_value":"azul"}
    - slot{"color_value":"azul"}
    - action_grafica_hist
    - slot{"senal":null}
    - slot{"fecha":null}
    - slot{"fecha":null}
    - slot{"color_value":null}
    - slot{"tipo_grafica":null}


## test 3
* grafica{"senal":"cic0009"}
   - slot{"senal": "cic0009"}
   - utter_ask_tipo_grafica
* grafica_serie{"tipo_grafica":"serie"}
   - slot{"tipo_grafica":"serie"}
   - utter_ask_tipo_serie
* mark{"mark_value": "no"}
    - slot{"mark_value": "no"}
    - action_grafica_serie
    - slot{"senal": null}
    - slot{"fecha": null}
    - slot{"fecha": null}
    - slot{"mark_value": null}
    - slot{"tipo_grafica": null}
* agradecer
   - utter_agradecer
* saludo
   - utter_saludo
* informacion{"senal":"CIC0012", "unidad":"unidad","descripcion":"descripcion","tipo":"tipo"}
    - slot{"senal":"CIC0012"}
    - slot{"unidad":"unidad"}
    - slot{"descripcion":"descripcion"}
    - slot{"tipo":"tipo"}
    - action_informacion
    - slot{"senal":null}
    - slot{"descripcion":null}
    - slot{"unidad":null}
    - slot{"tipo":null}
* buen_humor
   - utter_buen_humor
* grafica_hist{"senal": "CIC0010", "tipo_grafica":"histograma"}
   - slot{"senal": "CIC0010"}
   - slot{"tipo_grafica":"histograma"}
   - utter_ask_tipo_hist
* color{"color_value":"azul"}
    - slot{"color_value":"azul"}
    - action_grafica_hist
    - slot{"senal":null}
    - slot{"fecha":null}
    - slot{"fecha":null}
    - slot{"color_value":null}
    - slot{"tipo_grafica":null}
* descripcion{"fecha": "2017-02-01", "senal":"cic0011"}
    - slot{"fecha": ["2016-09-25", "2017-02-01"]}
    - slot{"senal":"cic0011"}
    - action_descripcion
    - slot{"senal": null}
    - slot{"fecha": null}
* despedida
   - utter_ask_feedback
* feedback{"feedback_value":"negativo"}
   - slot{"feedback_value":"negativo"}
   - utter_feedback_neg
   - utter_despedida


## test 4
* saludo
   - utter_saludo
* descripcion{"senal":"CIC0003"}
    - slot{"senal":"cic0002"}
    - action_descripcion
    - slot{"senal": null}
    - slot{"fecha": null}
* grafica{"fecha":"2018-10-03"}
   - slot{"fecha":["2017-08-29", "2018-10-03"]}
   - utter_ask_senal
* grafica{"senal":"cic0013"}
   - slot{"senal": "cic0013"}
   - utter_ask_tipo_grafica
* grafica_hist{"tipo_grafica":"histograma"}
   - slot{"tipo_grafica":"histograma"}
   - utter_ask_tipo_hist
* color{"color_value":"verde"}
    - slot{"color_value":"verde"}
    - action_grafica_hist
    - slot{"senal":null}
    - slot{"fecha":null}
    - slot{"fecha":null}
    - slot{"color_value":null}
    - slot{"tipo_grafica":null}
* grafica_serie{"fecha":"2018-03-17", "tipo_grafica":"serie","senal":"CIC0010"}
   - slot{"fecha":["2017-12-23", "2018-03-17"]}
    - slot{"senal":"CIC0010"}
    - slot{"tipo_grafica":"serie"}
    - utter_ask_tipo_serie
* mark{"mark_value":"no"}
    - slot{"mark_value":"no"}
    - action_grafica_serie
    - slot{"senal":null}
    - slot{"fecha":null}
    - slot{"fecha":null}
    - slot{"mark_value":null}
    - slot{"tipo_grafica":null}
* agradecer
   - utter_agradecer
* informacion{"tipo":"tipo", "unidad":"unidad"}
    - slot{"tipo":"tipo"}
    - slot{"unidad":"unidad"}
    - utter_ask_senal
* dar_senal{"senal": "cic0011"}
    - slot{"senal": "cic0011"}
    - action_informacion
    - slot{"senal": null}
    - slot{"descripcion": null}
    - slot{"unidad": null}
    - slot{"tipo": null}
* buen_humor
   - utter_buen_humor
* despedida
   - utter_ask_feedback
* feedback{"feedback_value":"positivo"}
   - slot{"feedback_value":"positivo"}
   - utter_feedback_pos
   - utter_despedida