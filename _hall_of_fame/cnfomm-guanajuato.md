---
title: Concurso Nacional Femenil de la Olimpiada Mexicana de Matemáticas
urlname: cnfomm-guanajuato
logo-title: ../assets/img/Logo-cnfomm.png
layout: home
---
<!-- Ésta es, por ahora, la mejor manera de hacer esto, porque los equipos de la Femenil son un desmadre que no puede ser formateadas como yaml's (como con las otras páginas). Si se te ocurre algo mejor, inténtalo. - Joshua -->
  {% assign years = "" | split: "" %}
  {% for participante in site.data.historico.cnfomm_guanajuato%}
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
        <th scope="col">Nivel</th>
        <th scope="col">Nombre</th>
        <th scope="col">Logro</th>
        <th scope="col">Logro en equipo</th>
      </tr>
    </thead>
    <tbody>
      {% assign niveles = "Nivel 1, Nivel 2" | split: ", " %}
      {% for nivel in niveles %}
        {% assign participants_in_level = false %}
        {% for participante in site.data.historico.cnfomm_guanajuato %}
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
            <td>{{participante.Logro_en_equipo}}</td>
          </tr>
          {% endif %}
        {% endfor %}
      {% endfor %}
    </tbody>
  </table>
  {% endfor %}
</div>