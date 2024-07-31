---
title: Olimpiada Mexicana de Matemáticas
urlname: omm-guanajuato
logo-title: ../assets/img/Logo-omm.png
layout: home
---

  {% assign years = "" | split: "" %}
  {% for participante in site.data.omm_guanajuato_historico%}
    {% assign year = participante.Year | strip %}
    {% unless years contains year %}
      {% assign years = years | push: year %}
    {% endunless %}
  {% endfor %}
  {% assign sorted_years = years | sort %}

  <div class= "row">
  {% for year in sorted_years reversed %}
  <h2 class="text-center">{{year}}</h2>
  <table class="table table-dark table-hover">
    <thead>
      <tr>
        <th scope="col">Nombre</th>
        <th scope="col">Logro</th>
      </tr>
    </thead>
    <tbody>
    {% for participante in site.data.omm_guanajuato_historico%}
    {% if participante.Year contains year %}
    <tr>
      <td>{{participante.Nombre}}</td>
      <td>{{participante.Logro}}</td>
    </tr>
    {% endif %}
    {% endfor %}
    </tbody>
  </table>
  {% endfor %}
</div>