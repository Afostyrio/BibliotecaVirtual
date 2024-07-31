---
title: Olimpiada Mexicana de Matemáticas para Educación Básica
urlname: ommeb-guanajuato
logo-title: ../assets/img/Logo-ommeb.png
layout: home
---
  {% assign years = "" | split: "" %}
  {% for participante in site.data.ommeb_guanajuato_historico%}
    {% assign year = participante.Year | strip %}
    {% unless years contains year %}
      {% assign years = years | push: year %}
    {% endunless %}
  {% endfor %}
  {% assign sorted_years = years | sort  %}

  <div class= "row">
  {% for year in sorted_years reversed%}
  <h2 class="text-center">{{year}}</h2>
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
      {% assign niveles = "Nivel 1, Nivel 2, Nivel 3" | split: ", " %}
      {% for nivel in niveles %}
        {% assign participants_in_level = false %}
        {% assign included_team_achievement = false %}
        {% for participante in site.data.ommeb_guanajuato_historico %}
          {% if participante.Year contains year and participante.Nivel contains nivel %}
            {% if participants_in_level == false %}
              <tr>
                <td rowspan="3" class= "align-middle text-center">{{nivel}}</td>
                {% assign participants_in_level = true %}
            {% else %}
              <tr>
            {% endif %}
            <td>{{participante.Nombre}}</td>
            <td>{{participante.Logro}}</td>
            {% if included_team_achievement == false %}
              <td rowspan="3" class= "align-middle text-center">{{participante.Logro_en_equipo}}</td>
              {% assign included_team_achievement = true %}
            {% endif %}
          </tr>
          {% endif %}
        {% endfor %}
      {% endfor %}
    </tbody>
  </table>
  {% endfor %}
</div>