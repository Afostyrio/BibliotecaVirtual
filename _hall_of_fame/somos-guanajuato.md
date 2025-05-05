---
title: Todos los olímpicos
urlname: somos-guanajuato
logo-title:
layout: home
altname: ¡Todos están aquí!
---
<div class= "row">
  {% for olympian in site.data.historico.somos_guanajuato %}
  <h2 class="text-center">{{olympian.name}}</h2>
  {% for item in olympian.years %}
  <h3>{{item.year}}</h3>
  <table class="table table-dark table-hover">
    <thead>
      <tr>
        <th scope="col">Olimpiada</th>
        <th scope="col">Nivel</th>
        <th scope="col">Logro</th>
        <th scope="col">Logro en equipo</th>
      </tr>
    </thead>
    <tbody>
      {% for olympiad in item.olympiads %}
      <tr>
        <td>{{olympiad.olympiad}}</td>
        <td>{{olympiad.level}}</td>
        <td>{{olympiad.achievement}}</td>
        <td>{{olympiad.team_achievement}}</td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
  {% endfor %}
  {% endfor %}
</div>