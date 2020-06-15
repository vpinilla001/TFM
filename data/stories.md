## saludo 1
* saludo
   - utter_saludo

## despedida 1 
* despedida
   - utter_ask_feedback
* feedback{"feedback_value":"positivo"}
   - slot{"feedback_value":"positivo"}
   - utter_feedback_pos
   - utter_despedida
   
## despedida 2
* despedida
   - utter_ask_feedback
* feedback{"feedback_value":"negativo"}
   - slot{"feedback_value":"negativo"}
   - utter_feedback_neg
   - utter_despedida

## agradecer 1
* agradecer
   - utter_agradecer
   
## buen humor 1
* buen_humor
   - utter_buen_humor

## grafica 1
* grafica
   - utter_ask_senal

## grafica 2
* grafica{"senal": "cic0005"}
   - slot{"senal": "cic0005"}
   - utter_ask_tipo_grafica

## grafica 3
* grafica{"senal": "cic0005", "fecha":"2018-05-05"}
   - slot{"senal": "cic0005"}
   - slot{"fecha":["2017-05-05", "2018-05-05"]}
   - utter_ask_tipo_grafica

## grafica 4
* grafica
   - utter_ask_senal
* grafica{"senal":"CIC0011"}
   - slot{"senal": "cic0011"}
   - utter_ask_tipo_grafica
* grafica_serie{"tipo_grafica":"serie"}
   - slot{"tipo_grafica":"serie"}
   - utter_ask_tipo_serie

## grafica 5
* grafica{"fecha":"2018-05-05"}
   - slot{"fecha":["2017-05-05", "2018-05-05"]}
   - utter_ask_senal
* grafica{"senal":"cic0005"}
   - slot{"senal": "cic0005"}
   - utter_ask_tipo_grafica
* grafica_hist{"tipo_grafica":"histograma"}
   - slot{"tipo_grafica":"histograma"}
   - utter_ask_tipo_hist

## grafica 6
* grafica{"fecha":"2018-04-15", "senal":"cic0013"}
   - slot{"fecha":["2017-12-21", "2018-04-15"]}
   - slot{"senal": "cic0013"}
   - utter_ask_tipo_grafica

## grafica serie 1
* grafica_serie{"senal": "cic0005", "fecha":"2017-05-05", "tipo_grafica":"serie"}
   - slot{"senal": "cic0005"}
   - slot{"fecha":["2017-05-05", "2018-05-05"]}
   - slot{"tipo_grafica":"serie"}
   - utter_ask_tipo_serie

## grafica serie 2
* grafica{"senal":"cic0001","fecha":"2018-11-06"}
    - slot{"fecha":["2016-03-06", "2018-11-06"]}
    - slot{"senal":"cic0001"}
    - utter_ask_tipo_grafica
* grafica_serie{"tipo_grafica":"serie"}
    - slot{"tipo_grafica":"serie"}
    - utter_ask_tipo_serie
* mark{"mark_value":"si"}
    - slot{"mark_value":"si"}
    - action_grafica_serie
    - slot{"senal":null}
    - slot{"fecha":null}
    - slot{"mark_value":null}
    - slot{"tipo_grafica":null}
* despedida
    - utter_ask_feedback
* feedback{"feedback_value":"positivo"}
   - slot{"feedback_value":"positivo"}
   - utter_feedback_pos
   - utter_despedida

## grafica serie 3
* saludo
    - utter_saludo
* grafica_serie{"tipo_grafica":"serie","senal":"cic0005","fecha":"2018-05-05"}
    - slot{"tipo_grafica":"serie"}
    - slot{"senal":"cic0005"}
    - slot{"fecha":["2017-05-05", "2018-05-05"]}
    - utter_ask_tipo_serie
* mark{"mark_value":"no"}
    - slot{"mark_value":"no"}
    - action_grafica_serie
    - slot{"senal":null}
    - slot{"fecha":null}
    - slot{"mark_value":null}
    - slot{"tipo_grafica":null}

##grafica serie 4
* saludo 
   - utter_saludo
* grafica_serie{"tipo_grafica": "serie"}
    - slot{"tipo_grafica": "serie"}
   - utter_ask_senal
* dar_senal{"senal": "cic0004"}
   - slot{"senal": "cic0004"}
   - utter_ask_tipo_serie   
* mark{"mark_value": "si"}
   - slot{"mark_value": "si"}
   - action_grafica_serie
   - slot{"senal":null}
   - slot{"fecha":null}
   - slot{"mark_value":null}
   - slot{"tipo_grafica":null}
* agradecer
   - utter_agradecer

## grafica serie 5
* saludo
    - utter_saludo
* grafica_serie{"senal":"cic0002","fecha":"2018-05-05", "tipo_grafica":"serie"}
    - slot{"fecha":["2017-05-05", "2018-05-05"]}
    - slot{"senal":"cic0002"}
    - slot{"tipo_grafica":"serie"}
    - utter_ask_tipo_serie
* mark{"mark_value":"si"}
    - slot{"mark_value":"si"}
    - action_grafica_serie
    - slot{"senal":null}
    - slot{"fecha":null}
    - slot{"mark_value":null}
    - slot{"tipo_grafica":null}
* despedida
    - utter_ask_feedback
* feedback{"feedback_value":"negativo"}
   - slot{"feedback_value":"negativo"}
   - utter_feedback_neg
   - utter_despedida

## grafica serie 6
* grafica_serie{"tipo_grafica":"serie","fecha":"2018-05-05"}
    - slot{"fecha":["2017-05-05", "2018-05-05"]}
    - slot{"tipo_grafica":"serie"}
    - utter_ask_senal

## grafica serie 7
* grafica_serie{"tipo_grafica":"serie"}
    - slot{"tipo_grafica":"serie"}
    - utter_ask_senal
* dar_senal{"senal":"cic0003"}
    - slot{"senal":"cic0003"}
    - utter_ask_tipo_serie

## grafica serie 8
* grafica_serie{"tipo_grafica":"serie","fecha":"2018-03-03"}
    - slot{"fecha":["2017-04-04", "2018-03-03"]}
    - slot{"tipo_grafica":"serie"}
    - utter_ask_senal

## grafica serie 9
* saludo
    - utter_saludo
* grafica{"senal":"CIC0007"}
    - slot{"senal":"CIC0007"}
    - utter_ask_tipo_grafica
* grafica_serie{"tipo_grafica":"serie"}
    - slot{"tipo_grafica":"serie"}
    - utter_ask_tipo_serie
* mark{"mark_value":"si"}
    - slot{"mark_value":"si"}
    - action_grafica_serie
    - slot{"senal":null}
    - slot{"fecha":null}
    - slot{"mark_value":null}
    - slot{"tipo_grafica":null}
* buen_humor
    - utter_buen_humor
* despedida
    - utter_ask_feedback
* feedback{"feedback_value":"positivo"}
   - slot{"feedback_value":"positivo"}
   - utter_feedback_pos
   - utter_despedida

## grafica serie 10
* grafica_serie{"tipo_grafica":"serie"}
    - slot{"tipo_grafica":"serie"}
    - utter_ask_senal
* grafica_serie{"tipo_grafica":"serie","senal":"cic0010"}
    - slot{"senal":"cic0010"}
    - slot{"tipo_grafica":"serie"}
    - utter_ask_tipo_serie
* mark{"mark_value":"no"}
    - slot{"mark_value":"no"}
    - action_grafica_serie
    - slot{"senal":null}
    - slot{"fecha":null}
    - slot{"mark_value":null}
    - slot{"tipo_grafica":null}

## grafica serie 11
* grafica_serie{"tipo_grafica":"serie"}
    - slot{"tipo_grafica":"serie"}
    - utter_ask_senal
* dar_senal{"senal":"cic0012"}
    - slot{"senal":"cic0012"}
    - utter_ask_tipo_serie
* mark{"mark_value":"si"}
    - slot{"mark_value":"si"}
    - action_grafica_serie
    - slot{"senal":null}
    - slot{"fecha":null}
    - slot{"mark_value":null}
    - slot{"tipo_grafica":null}
* buen_humor
   - utter_buen_humor

## grafica serie 12
* grafica_serie{"tipo_grafica":"serie","fecha":"2018-09-12"}
    - slot{"fecha":["2017-05-09", "2018-09-12"]}
    - slot{"tipo_grafica":"serie"}
    - utter_ask_senal

## grafica serie 13
* grafica_serie{"tipo_grafica":"serie"}
    - slot{"tipo_grafica":"serie"}
    - utter_ask_senal
* dar_senal{"senal":"cic0002"}
    - slot{"senal":"cic0002"}
    - utter_ask_tipo_serie

## grafica serie 14
* grafica_serie{"tipo_grafica":"serie"}
    - slot{"tipo_grafica":"serie"}
    - utter_ask_senal
* dar_senal{"senal":"cic0010"}
    - slot{"senal":"cic0010"}
    - utter_ask_tipo_serie
    
## grafica serie 15
* grafica_serie{"tipo_grafica":"serie","fecha":"2018-01-12"}
    - slot{"fecha":["2016-09-15", "2018-01-12"]}
    - slot{"tipo_grafica":"serie"}
    - utter_ask_senal
* dar_senal{"senal":"cic0002"}
    - slot{"senal":"cic0002"}
    - utter_ask_tipo_serie

## grafica hist 1
* grafica_hist{"tipo_grafica":"histograma","fecha":"2018-06-04"}
    - slot{"fecha":["2017-05-05", "2018-06-04"]}
    - slot{"tipo_grafica":"histograma"}
    - utter_ask_senal

## grafica hist 2  
* grafica_serie{"tipo_grafica":"histograma","fecha":"2017-02-05"}
    - slot{"fecha":["2016-11-07", "2017-02-05"]}
    - slot{"tipo_grafica":"histograma"}
    - utter_ask_senal
* dar_senal{"senal":"cic0007"}
    - slot{"senal":"cic0007"}
    - utter_ask_tipo_hist  
   
## grafica hist 3
* grafica_hist{"tipo_grafica":"histograma"}
    - slot{"tipo_grafica":"histograma"}
    - utter_ask_senal

##grafica hist 4
* grafica_hist{"tipo_grafica":"histograma","senal":"cic0002"}
    - slot{"senal":"cic0002"}
    - slot{"tipo_grafica":"histograma"}
    - utter_ask_tipo_hist
* color{"color_value":"rojo"}
    - slot{"color_value":"rojo"}
    - action_grafica_hist
    - slot{"senal":null}
    - slot{"fecha":null}
    - slot{"color_value":null}
    - slot{"tipo_grafica":null}

## grafica hist 5
* grafica_hist{"senal": "cic0005", "fecha":"2018-05-05", "tipo_grafica":"histograma"}
   - slot{"senal": "cic0005"}
   - slot{"fecha":["2018-05-05", "2017-05-05"]}
   - slot{"tipo_grafica":"histograma"}
   - utter_ask_tipo_hist

## grafica hist 6
* grafica{"senal": "cic0001","fecha": "2018-06-07"}
   - slot{"senal": "cic0001"}
   - slot{"fecha": ["2018-01-17", "2018-06-07"]}
   - utter_ask_tipo_grafica
* grafica_hist{"tipo_grafica": "histograma"}
   - slot{"tipo_grafica": "histograma"}
   - utter_ask_tipo_hist
* color{"color_value": "verde"}
   - slot{"color_value": "verde"}
   - action_grafica_hist
   - slot{"senal":null}
   - slot{"fecha":null}
   - slot{"color_value":null}
   - slot{"tipo_grafica":null}
* buen_humor
   - utter_buen_humor

## grafica hist 7
* grafica_hist{"tipo_grafica":"histograma","fecha":"2017-12-23"}
    - slot{"fecha":["2016-11-11", "2017-12-23"]}
    - slot{"tipo_grafica":"histograma"}
    - utter_ask_senal

## grafica hist 8
* saludo
    - utter_saludo
* grafica{"senal":"cic0001","fecha":"2018-11-06"}
    - slot{"fecha":["2016-03-06", "2018-11-06"]}
    - slot{"senal":"cic0001"}
    - utter_ask_tipo_grafica
* grafica_hist{"tipo_grafica":"histograma"}
    - slot{"tipo_grafica":"histograma"}
    - utter_ask_tipo_hist
* color{"color_value":"rojo"}
    - slot{"color_value":"rojo"}
    - action_grafica_hist
    - slot{"senal":null}
    - slot{"fecha":null}
    - slot{"color_value":null}
    - slot{"tipo_grafica":null}
* agradecer
    - utter_agradecer

## grafica hist 9
* grafica_hist{"tipo_grafica":"histograma","fecha":"2017-11-25"}
    - slot{"fecha":["2016-08-29", "2017-11-25"]}
    - slot{"tipo_grafica":"histograma"}
    - utter_ask_senal

## grafica hist 10
* grafica_hist{"tipo_grafica": "histograma"}
    - slot{"tipo_grafica": "histograma"}
    - utter_ask_senal
* dar_senal{"senal": "cic0011"}
    - slot{"senal": "cic0011"}
    - utter_ask_tipo_hist
* color{"color_value": "azul"}
    - slot{"color_value": "azul"}
    - action_grafica_hist
    - slot{"senal": null}
    - slot{"fecha": null}
    - slot{"color_value": null}
    - slot{"tipo_grafica": null}

## grafica hist 11
* grafica_hist{"tipo_grafica": "histograma","fecha":"2018-04-12"}
    - slot{"fecha":["2017-11-29", "2018-04-125"]}
    - slot{"tipo_grafica": "histograma"}
    - utter_ask_senal
* dar_senal{"senal": "cic0001"}
    - slot{"senal": "cic0001"}
    - utter_ask_tipo_hist
* color{"color_value": "azul"}
    - slot{"color_value": "azul"}
    - action_grafica_hist
    - slot{"senal": null}
    - slot{"fecha": null}
    - slot{"color_value": null}
    - slot{"tipo_grafica": null}

## informacion 1
* informacion{"tipo":"tipo"}
    - slot{"tipo":"tipo"}
    - utter_ask_senal

## informacion 2
* informacion{"descripcion":"descripcion"}
    - slot{"descripcion":"descripcion"}
    - utter_ask_senal
* dar_senal{"senal":"cic0011"}
    - slot{"senal":"cic0011"}
    - action_informacion
    - slot{"senal":null}
    - slot{"descripcion":null}
    - slot{"unidad":null}
    - slot{"tipo":null}

## informacion 3
* informacion{"descripcion":"descripcion","unidad":"unidad"}
    - slot{"descripcion":"descripcion"}
    - slot{"unidad":"unidad"}
    - utter_ask_senal
* dar_senal{"senal":"cic0006"}
    - slot{"senal":"cic0006"}
    - action_informacion
    - slot{"senal":null}
    - slot{"descripcion":null}
    - slot{"unidad":null}
    - slot{"tipo":null}

## informacion 4  
* informacion{"unidad":"unidad"}
    - slot{"unidad":"unidad"}
    - utter_ask_senal
* dar_senal{"senal":"CIC0008"}
    - slot{"senal":"CIC0008"}
    - action_informacion
    - slot{"senal":null}
    - slot{"descripcion":null}
    - slot{"unidad":null}
    - slot{"tipo":null}

## informacion 5
* informacion
    - utter_ask_senal
* dar_senal{"senal":"cic0006"}
    - action_informacion
    - slot{"senal":null}
    - slot{"descripcion":null}
    - slot{"unidad":null}
    - slot{"tipo":null}
* buen_humor
   - utter_buen_humor
* agradecer
    - utter_agradecer

## informacion 6
* informacion{"tipo":"tipo","unidad":"unidad"}
    - slot{"tipo":"tipo"}
    - slot{"unidad":"unidad"}
    - utter_ask_senal

## informacion 7
* informacion
    - utter_ask_senal
* dar_senal{"senal":"CIC0005"}
    - slot{"senal":"CIC0005"}
    - action_informacion
    - slot{"senal":null}
    - slot{"descripcion":null}
    - slot{"unidad":null}
    - slot{"tipo":null}
* agradecer
    - utter_agradecer

## informacion 8
* informacion{"senal": "cic0011"}
   - slot{"senal": "cic0011"}
   - action_informacion
   - slot{"senal": null}
   - slot{"descripcion": null}
   - slot{"unidad": null}
   - slot{"tipo": null}
* buen_humor
   - utter_buen_humor

## informacion 9
* informacion{"senal": "cic0011", "tipo": "tipo", "descripcion":"descripcion"}
   - slot{"senal": "cic0011"}
   - slot{"tipo": "tipo"}
   - slot{"descripcion":"descripcion"}
   - action_informacion
   - slot{"senal": null}
   - slot{"descripcion": null}
   - slot{"unidad": null}
   - slot{"tipo": null}

## informacion 10
* saludo
    - utter_saludo
* informacion{"descripcion":"descripcion"}
    - slot{"descripcion":"descripcion"}
    - utter_ask_senal
* dar_senal{"descripcion":"descripcion","senal":"cic0003"}
    - slot{"descripcion":"descripcion"}
    - slot{"senal":"cic0003"}
    - action_informacion
    - slot{"senal":null}
    - slot{"descripcion":null}
    - slot{"unidad":null}
    - slot{"tipo":null}

## informacion 11
* informacion{"unidad":"unidad","tipo":"tipo","senal":"cic0011"}
    - slot{"senal":"cic0011"}
    - slot{"tipo":"tipo"}
    - slot{"unidad":"unidad"}
    - action_informacion
    - slot{"senal":null}
    - slot{"descripcion":null}
    - slot{"unidad":null}
    - slot{"tipo":null}
* despedida
    - utter_ask_feedback
* feedback{"feedback_value":"negativo"}
   - slot{"feedback_value":"negativo"}
   - utter_feedback_neg
   - utter_despedida

## informacion 12  
* informacion{"unidad":"unidad"}
    - slot{"unidad":"unidad"}
    - utter_ask_senal
* dar_senal{"senal":"cic0002"}
    - slot{"senal":"cic0002"}
    - action_informacion
    - slot{"senal":null}
    - slot{"descripcion":null}
    - slot{"unidad":null}
    - slot{"tipo":null}

## informacion 13
* informacion{"descripcion":"descripcion","unidad":"unidad"}
    - slot{"descripcion":"descripcion"}
    - slot{"unidad":"unidad"}
    - utter_ask_senal
* dar_senal{"senal":"cic0001"}
    - slot{"senal":"cic0001"}
    - action_informacion
    - slot{"senal":null}
    - slot{"fecha":null}

## informacion 14
* informacion{"unidad":"unidad","descripcion":"descripcion"}
    - slot{"descripcion":"descripcion"}
    - slot{"unidad":"unidad"}
    - utter_ask_senal
* dar_senal{"senal":"CIC0009"}
    - slot{"senal":"CIC0009"}
    - action_informacion
    - slot{"senal":null}
    - slot{"descripcion":null}
    - slot{"unidad":null}
    - slot{"tipo":null}

## descripcion 1
* descripcion{"fecha":"2018-05-05"}
    - slot{"fecha":["2017-05-05", "2018-05-05"]}
    - utter_ask_senal
* buen_humor
   - utter_buen_humor

## descripcion 2
* descripcion
    - utter_ask_senal
* dar_senal{"senal":"cic0001"}
    - slot{"senal":"cic0001"}
    - action_descripcion
    - slot{"senal":null}
    - slot{"fecha":null}

## descripcion 3
* descripcion
    - utter_ask_senal
* dar_senal{"senal":"cic0002"}
    - slot{"senal":"cic0002"}
    - action_descripcion
    - slot{"senal":null}
    - slot{"fecha":null}

## descripcion 4
* descripcion
    - utter_ask_senal
* dar_senal{"senal":"cic0003"}
    - slot{"senal":"cic0003"}
    - action_descripcion
    - slot{"senal":null}
    - slot{"fecha":null}

## descripcion 5
* descripcion
    - utter_ask_senal
* dar_senal{"senal":"cic0004"}
    - slot{"senal":"cic0004"}
    - action_descripcion
    - slot{"senal":null}
    - slot{"fecha":null}
* despedida
    - utter_ask_feedback
* feedback{"feedback_value":"positivo"}
   - slot{"feedback_value":"positivo"}
   - utter_feedback_pos
   - utter_despedida

## descripcion 6
* descripcion
    - utter_ask_senal
* dar_senal{"senal":"cic0005"}
    - slot{"senal":"cic0005"}
    - action_descripcion
    - slot{"senal":null}
    - slot{"fecha":null}

## descripcion 7
* descripcion
   - utter_ask_senal

## descripcion 8
* descripcion{"senal": "cic0006"}
   - slot{"senal": "cic0006"}
   - action_descripcion
   - slot{"senal":null}
   - slot{"fecha":null}

## descripcion 9
* descripcion{"senal": "cic0013", "fecha":"2017-04-03"}
   - slot{"senal": "cic0013"}
   - slot{"fecha":["2017-04-03", "2017-10-19"]}
   - action_descripcion
   - slot{"senal": "cic0013"}
   - action_descripcion
   - slot{"senal":null}
   - slot{"fecha":null}
* buen_humor
   - utter_buen_humor

## descripcion 10
* saludo
   - utter_saludo
* descripcion{"senal": "cic0007"}
   - slot{"senal": "cic0007"}
   - action_descripcion
   - slot{"senal":null}
   - slot{"fecha":null}
* buen_humor
   - utter_buen_humor

## descripcion 11
* saludo
   - utter_saludo
* descripcion
   - utter_ask_senal
* dar_senal{"senal": "cic0008"}
   - slot{"senal": "cic0008"}
   - action_descripcion
   - slot{"senal":null}
   - slot{"fecha":null}
* buen_humor
   - utter_buen_humor

## descripcion 12
* descripcion{"senal":"cic0011","fecha":"2018-05-05"}
    - slot{"fecha":["2017-05-05", "2018-05-05"]}
    - slot{"senal":"cic0011"}
    - action_descripcion
    - slot{"senal":null}
    - slot{"fecha":null}
* despedida
    - utter_ask_feedback
* feedback{"feedback_value":"negativo"}
   - slot{"feedback_value":"negativo"}
   - utter_feedback_neg
   - utter_despedida

## descripcion 13
* descripcion
    - utter_ask_senal
* dar_senal{"senal":"CIC0009"}
    - slot{"senal":"CIC0009"}
    - action_descripcion
    - slot{"senal":null}
    - slot{"fecha":null}

## descripcion 14
* descripcion{"senal":"cic0006", "fecha":"2018-05-05"}
    - slot{"fecha":["2017-05-05", "2018-05-05"]}
    - slot{"senal":"cic0006"}
    - action_descripcion
    - slot{"senal":null}
    - slot{"fecha":null}
* despedida
    - utter_ask_feedback
* feedback{"feedback_value":"positivo"}
   - slot{"feedback_value":"positivo"}
   - utter_feedback_pos
   - utter_despedida

##descripcion 15
* descripcion{"fecha":"2018-05-05"}
    - slot{"fecha":["2017-05-05", "2018-05-05"]}
    - utter_ask_senal
* dar_senal{"senal":"cic0006"}
    - slot{"senal":"cic0006"}
    - action_descripcion
    - slot{"senal":null}
    - slot{"fecha":null}

##descripcion 16
* descripcion{"fecha":"2018-05-05"}
    - slot{"fecha":["2017-05-05", "2018-05-05"]}
    - utter_ask_senal
* dar_senal{"senal":"cic0007"}
    - slot{"senal":"cic0007"}
    - action_descripcion
    - slot{"senal":null}
    - slot{"fecha":null}

## descripcion 17
* descripcion
    - utter_ask_senal
* dar_senal{"senal":"cic0010"}
    - slot{"senal":"cic0010"}
    - action_descripcion
    - slot{"senal":null}
    - slot{"fecha":null}

## descripcion 16
* descripcion{"fecha":"2017-11-14"}
    - slot{"fecha":["2017-08-26", "2017-11-14"]}
    - utter_ask_senal  
* dar_senal{"senal":"cic0001"}
    - slot{"senal":"cic0001"}
    - action_descripcion
    - slot{"senal":null}
    - slot{"fecha":null}

## descripcion 17
* descripcion{"fecha":"2017-02-09"}
    - slot{"fecha":["2016-12-25", "2017-02-09"]}
    - utter_ask_senal  
* dar_senal{"senal":"cic0002"}
    - slot{"senal":"cic0002"}
    - action_descripcion
    - slot{"senal":null}
    - slot{"fecha":null}

## mark 1
* mark{"mark_value":"no"}
   - slot{"mark_value":"no"}
   - action_grafica_serie
   - slot{"senal":null}
   - slot{"fecha":null}
   - slot{"mark_value":null}
   - slot{"tipo_grafica":null}

## color 1
* color{"color_value":"verde"}
   - slot{"color_value":"verde"}
   - action_grafica_hist
   - slot{"senal":null}
   - slot{"fecha":null}
   - slot{"color_value":null}
   - slot{"tipo_grafica":null}

## mix 1
* grafica{"senal":"cic0005","fecha":"2018-05-05"}
    - slot{"fecha":["2017-05-05", "2018-05-05"]}
    - slot{"senal":"cic0005"}
    - utter_ask_tipo_grafica
* grafica_hist{"tipo_grafica":"histograma"}
    - slot{"tipo_grafica":"histograma"}
    - utter_ask_tipo_hist
* color{"color_value":"verde"}
    - slot{"color_value":"verde"}
    - action_grafica_hist
    - slot{"senal":null}
    - slot{"fecha":null}
    - slot{"color_value":null}
    - slot{"tipo_grafica":null}
* agradecer
    - utter_agradecer
* informacion{"unidad":"unidad","tipo":"tipo","senal":"cic0011"}
    - slot{"senal":"cic0011"}
    - slot{"tipo":"tipo"}
    - slot{"unidad":"unidad"}
    - action_informacion
    - slot{"senal":null}
    - slot{"descripcion":null}
    - slot{"unidad":null}
    - slot{"tipo":null}
* descripcion
    - utter_ask_senal
* dar_senal{"senal":"CIC0002"}
    - slot{"senal":"CIC0002"}
    - action_descripcion
    - slot{"senal":null}
    - slot{"fecha":null}

## mix 2
* saludo
    - utter_saludo
* buen_humor
    - utter_buen_humor
* saludo
    - utter_saludo
* despedida
    - utter_ask_feedback
* feedback{"feedback_value":"positivo"}
   - slot{"feedback_value":"positivo"}
   - utter_feedback_pos
   - utter_despedida

## mix 3
* saludo
    - utter_saludo
* grafica{"tipo_grafica":"histograma","senal":"cic0001","fecha":"2018-01-01"}
    - slot{"tipo_grafica":"histograma"}
    - slot{"senal":"cic0001"}
    - slot{"fecha":["2016-08-27", "2018-01-01"]}
    - utter_ask_tipo_hist
* color{"color_value":"azul"}
    - slot{"color_value":"azul"}
    - action_grafica_hist
    - slot{"senal":null}
    - slot{"fecha":null}
    - slot{"color_value":null}
    - slot{"tipo_grafica":null}
* grafica{"tipo_grafica":"serie","senal":"CIC0002"}
    - slot{"senal":"CIC0002"}
    - slot{"tipo_grafica":"serie"}
    - utter_ask_tipo_serie
* mark{"mark_value":"no"}
    - slot{"mark_value":"no"}
    - action_grafica_serie
    - slot{"senal":null}
    - slot{"fecha":null}
    - slot{"mark_value":null}
    - slot{"tipo_grafica":null}

## mix 4
* saludo
    - utter_saludo
* grafica{"tipo_grafica":"histograma","senal":"cic0001","fecha":"2018-05-05"}
    - slot{"fecha":["2017-05-05", "2018-05-05"]}
    - slot{"senal":"cic0001"}
    - slot{"tipo_grafica":"histograma"}
    - utter_ask_tipo_hist
* color{"color_value":"rojo"}
    - slot{"color_value":"rojo"}
    - action_grafica_hist
    - slot{"senal":null}
    - slot{"fecha":null}
    - slot{"color_value":null}
    - slot{"tipo_grafica":null}
* grafica{"tipo_grafica":"serie","senal":"CIC0002"}
    - slot{"senal":"CIC0002"}
    - slot{"tipo_grafica":"serie"}
    - utter_ask_tipo_serie
* mark{"mark_value":"si"}
    - slot{"mark_value":"si"}
    - action_grafica_serie
    - slot{"senal":null}
    - slot{"fecha":null}
    - slot{"mark_value":null}
    - slot{"tipo_grafica":null}
* informacion{"unidad":"unidad","tipo":"tipo","senal":"cic0003"}
    - slot{"senal":"cic0003"}
    - slot{"tipo":"tipo"}
    - slot{"unidad":"unidad"}
    - action_informacion
    - slot{"senal":null}
    - slot{"descripcion":null}
    - slot{"unidad":null}
    - slot{"tipo":null}
* descripcion{"senal":"CIC0004", "fecha":"2017-12-12"}
    - slot{"fecha":["2016-12-12", "2017-12-12"]}
    - slot{"senal":"CIC0004"}
    - action_descripcion
    - slot{"senal":null}
    - slot{"fecha":null}
* buen_humor
    - utter_buen_humor
* despedida
    - utter_ask_feedback
* feedback{"feedback_value":"negativo"}
   - slot{"feedback_value":"negativo"}
   - utter_feedback_neg
   - utter_despedida
   
## mix 5
* descripcion
    - utter_ask_senal
* dar_senal{"senal": "cic0001"}
    - slot{"senal": "cic0001"}
    - action_descripcion
    - slot{"senal": null}
    - slot{"fecha": null}
* informacion
    - utter_ask_senal
* dar_senal{"senal": "cic0001"}
    - slot{"senal": "cic0001"}
    - action_informacion
    - slot{"senal": null}
    - slot{"descripcion": null}
    - slot{"unidad": null}
    - slot{"tipo": null}
* descripcion{"fecha": "2017-06-23"}
    - slot{"fecha": ["2016-05-09", "2017-06-23"]}
    - utter_ask_senal
* dar_senal{"senal": "CIC0001"}
    - slot{"senal": "CIC0001"}
    - action_descripcion
    - slot{"senal": null}
    - slot{"fecha": null}
* grafica{"tipo_grafica": "serie", "fecha": "2018-09-14"}
    - slot{"fecha": ["2016-11-25", "2018-09-14"]}
    - slot{"tipo_grafica": "serie"}
    - utter_ask_senal
* dar_senal{"senal": "cic0001"}
    - slot{"senal": "cic0001"}
    - utter_ask_tipo_serie
* mark{"mark_value": "si"}
    - slot{"mark_value": "si"}
    - action_grafica_serie
    - slot{"senal": null}
    - slot{"fecha": null}
    - slot{"mark_value": null}
    - slot{"tipo_grafica": null}
* grafica
    - utter_ask_senal
* dar_senal{"senal": "cic0001"}
    - slot{"senal": "cic0001"}
    - utter_ask_tipo_grafica
* grafica_serie{"tipo_grafica": "serie"}
    - slot{"tipo_grafica": "serie"}
    - utter_ask_tipo_serie
* mark{"mark_value": "si"}
    - slot{"mark_value": "si"}
    - action_grafica_serie
    - slot{"senal": null}
    - slot{"fecha": null}
    - slot{"mark_value": null}
    - slot{"tipo_grafica": null}
* grafica{"tipo_grafica": "histograma", "fecha": "2018-05-05"}
    - slot{"fecha": ["2017-05-05", "2018-05-05"]}
    - slot{"tipo_grafica": "histograma"}
    - utter_ask_senal
* dar_senal{"senal": "cic0001"}
    - slot{"senal": "cic0001"}
    - utter_ask_tipo_hist
* color{"color_value": "rojo"}
    - slot{"color_value": "rojo"}
    - action_grafica_hist
    - slot{"senal": null}
    - slot{"fecha": null}
    - slot{"color_value": null}
    - slot{"tipo_grafica": null}

## mix 6
* descripcion
    - utter_ask_senal
* dar_senal
    - action_descripcion
* grafica
    - utter_ask_senal
* dar_senal{"senal": "cic0001"}
    - slot{"senal": "cic0001"}
    - utter_ask_tipo_grafica
* grafica_hist{"tipo_grafica": "histograma"}
    - slot{"tipo_grafica": "histograma"}
    - utter_ask_tipo_hist
* color{"color_value": "verde"}
    - slot{"color_value": "verde"}
    - action_grafica_hist
    - slot{"senal": null}
    - slot{"fecha": null}
    - slot{"color_value": null}
    - slot{"tipo_grafica": null}
* informacion
    - utter_ask_senal
* dar_senal{"senal": "cic0001"}
    - slot{"senal": "cic0001"}
    - action_informacion
    - slot{"senal": null}
    - slot{"descripcion": null}
    - slot{"unidad": null}
    - slot{"tipo": null}
* descripcion{"fecha": "2018-05-05"}
    - slot{"fecha": ["2017-08-05", "2018-05-05"]}
    - utter_ask_senal
* dar_senal{"senal": "cic0001"}
    - slot{"senal": "cic0001"}
    - action_descripcion
    - slot{"senal": null}
    - slot{"fecha": null}
* grafica_serie{"tipo_grafica": "serie", "fecha": "2018-05-05"}
    - slot{"fecha": ["2017-05-05", "2018-05-05"]}
    - slot{"tipo_grafica": "serie"}
    - utter_ask_senal
* dar_senal{"senal": "cic0001"}
    - slot{"senal": "cic0001"}
    - utter_ask_tipo_serie
* mark{"mark_value": "no"}
    - slot{"mark_value": "no"}
    - action_grafica_serie
    - slot{"senal": null}
    - slot{"fecha": null}
    - slot{"mark_value": null}
    - slot{"tipo_grafica": null}
* informacion{"tipo": "tipo"}
    - slot{"tipo": "tipo"}
    - utter_ask_senal
* dar_senal{"senal": "cic0001"}
    - slot{"senal": "cic0001"}
    - action_informacion
    - slot{"senal": null}
    - slot{"descripcion": null}
    - slot{"unidad": null}
    - slot{"tipo": null}
* grafica_hist{"tipo_grafica": "histograma"}
    - slot{"tipo_grafica": "histograma"}
    - utter_ask_senal
* dar_senal{"senal": "cic0001"}
    - slot{"senal": "cic0001"}
    - utter_ask_tipo_hist
* color{"color_value": "azul"}
    - slot{"color_value": "azul"}
    - action_grafica_hist
    - slot{"senal": null}
    - slot{"fecha": null}
    - slot{"color_value": null}
    - slot{"tipo_grafica": null}

## mix 7
* saludo
    - utter_saludo
* grafica{"fecha":"2018-05-07"}
    - slot{"fecha":["2016-11-12", "2018-05-07"]}
    - utter_ask_senal
* dar_senal{"senal":"cic0005"}
    - slot{"senal":"cic0005"}
    - utter_ask_tipo_grafica
* grafica_serie{"tipo_grafica":"serie"}
    - slot{"tipo_grafica":"serie"}
    - utter_ask_tipo_serie
    
    
## mix 8
* saludo
    - utter_saludo
* grafica{"fecha":"2018-05-07"}
    - slot{"fecha":["2016-11-12", "2018-05-07"]}
    - utter_ask_senal
* dar_senal{"senal":"cic0005"}
    - slot{"senal":"cic0005"}
    - utter_ask_tipo_grafica
* grafica_serie{"tipo_grafica":"serie"}
    - slot{"tipo_grafica":"serie"}
    - utter_ask_tipo_serie
* agradecer
    - utter_agradecer

