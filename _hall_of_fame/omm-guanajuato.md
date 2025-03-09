---
title: Olimpiada Mexicana de Matemáticas
urlname: omm-guanajuato
logo-title: ../assets/img/Logo-omm.png
layout: home
---

<div class= "row">
  {% for item in site.data.historico.omm_guanajuato reversed %}
  <h2 class="text-center">{{item.year}}</h2>
  <h3 class="text-center">{{item.location}}</h3>
  <table class="table table-dark table-hover">
    <thead>
      <tr>
        <th scope="col">Nombre</th>
        <th scope="col">Logro</th>
      </tr>
    </thead>
    <tbody>
    {% for participante in item.team%}
    <tr>
      <td>{{participante.name}}</td>
      <td>{{participante.achievement}}</td>
    </tr>
    {% endfor %}
    </tbody>
  </table>
  {% endfor %}
</div>