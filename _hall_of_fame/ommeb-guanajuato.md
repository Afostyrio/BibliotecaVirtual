---
title: Olimpiada Mexicana de Matemáticas para Educación Básica
urlname: ommeb-guanajuato
logo-title: ../assets/img/Logo-ommeb.png
layout: home
---
  <div class= "row">
  {% for item in site.data.historico.ommeb_guanajuato reversed%}
  <h2 class="text-center">{{item.year}}</h2>
  <h3 class="text-center">{{item.location}}</h3>
  <table class="table table-dark table-hover">
    <thead>
      <tr>
        <th scope="col">Nivel</th>
        <th scope="col">Nombre</th>
        <th scope="col">Logro</th>
        <th scope="col">Logro en equipo</th>
      </tr>
    </thead>
    <tbody>
      {% for level in item.levels %}
      <tr>
        <td rowspan="3" class= "align-middle text-center">{{ level.level }}</td>
        <td>{{level.team[0].name}}</td>
        <td>{{level.team[0].achievement}}</td>
        <td rowspan="3" class= "align-middle text-center">{{level.team_achievement}}</td>
      </tr>
      <tr>
        <td>{{level.team[1].name}}</td>
        <td>{{level.team[1].achievement}}</td>
      </tr>
      <tr>
        <td>{{level.team[2].name}}</td>
        <td>{{level.team[2].achievement}}</td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
  {% endfor %}
</div>