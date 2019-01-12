% calif.pl
% consult(calif).

%Hechos
alumno(luis).
alumno(jessica).
alumno(hector).
alumno(jaime).
alumno(laura).

%Relaciones
alumno_asiste(jessica,siempre).
alumno_asiste(luis,casisiempre).
alumno_asiste(laura,aveces).
alumno_asiste(jaime,muypoco).
alumno_asiste(hector,raravez).

porcentaje_asistencia(siempre,excelente).
porcentaje_asistencia(casisiempre,muybueno).
porcentaje_asistencia(constante,bueno).
porcentaje_asistencia(regular,regular).
porcentaje_asistencia(aveces,suficiente).
porcentaje_asistencia(poco,deficiente).
porcentaje_asistencia(muypoco,malo).
porcentaje_asistencia(devezencuando,muymalo).
porcentaje_asistencia(raravez,problematico).
porcentaje_asistencia(casinunca,vago).
porcentaje_asistencia(nunca,noexiste).

nivel_calif(excelente,10).
nivel_calif(muybueno,9).
nivel_calif(bueno,8).
nivel_calif(regular,7).
nivel_calif(suficiente,6).
nivel_calif(deficiente,5).
nivel_calif(malo,4).
nivel_calif(muymalo,3).
nivel_calif(problematico,2).
nivel_calif(vago,1).
nivel_calif(noexiste,0).

%regla
calificacion(X, Y):-alumno(X),
                    alumno_asiste(X,U),
                    porcentaje_asistencia(U,V),
                    nivel_calif(V,Y). 



