---
title: Olimpiada Mexicana de Matemáticas para Educación Básica
urlname: ommeb
logo-title: ../assets/img/Logo-ommeb.png
layout: home
---

{% for edition in site.data.ediciones_ommeb reversed %}
<div class="row">
	<div class="col mb-3">
	<h2 class="text-center">{{edition.year}}</h2>
	<h3 class="text-center">{{edition.location}}</h3>
  <h4>Individual</h4>
    <div class="row row-cols-1 row-cols-xl-4 row-cols-md-3 g-4">
    {% for level in edition.individual_levels %}
      <div class="col mx-auto">
        <div class="card h-100 mb-3">
          <a
            href="../assets/pdf/Nacionales/OMMEB/{{ edition.year }}-I-N{{ level.level }}.pdf"
            target="_blank"
            rel="noopener noreferrer"
          >
            <img
              height="150px"
              style="object-fit: contain;"
              class="card-img-top border-bottom bg-white"
              src="../assets/img/{{ edition.thumbnail }}"
              alt="OMMEB {{ item.year }} Individual Nivel {{ level.level }}">
          </a>
          <div class="card-body">
            <a
              href="{{ item.file | relative_url }}"
              target="_blank"
              class="card-link"
              rel="noopener noreferrer"
            >OMMEB {{ edition.year }} Individual Nivel {{ level.level }}</a>
          </div>
        </div>
      </div>
    {% endfor %}
    </div>
  <h4>Equipos</h4>
    <div class="row row-cols-1 row-cols-xl-4 row-cols-md-3 g-4">
    {% for level in edition.team_levels %}
      <div class="col mx-auto">
        <div class="card h-100 mb-3">
          <a
            href="../assets/pdf/Nacionales/OMMEB/{{ edition.year }}-I-N{{ level.level }}.pdf"
            target="_blank"
            rel="noopener noreferrer"
          >
            <img
              height="150px"
              style="object-fit: contain;"
              class="card-img-top border-bottom bg-white"
              src="../assets/img/{{ edition.thumbnail }}"
              alt="OMMEB {{ item.year }} Individual Nivel {{ level.level }}">
          </a>
          <div class="card-body">
            <a
              href="{{ item.file | relative_url }}"
              target="_blank"
              class="card-link"
              rel="noopener noreferrer"
            >OMMEB {{ edition.year }} Individual Nivel {{ level.level }}</a>
          </div>
        </div>
      </div>
    {% endfor %}
    </div>    
  </div>
</div>
{% endfor %}