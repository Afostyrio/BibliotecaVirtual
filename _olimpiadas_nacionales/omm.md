---
title: Olimpiada Mexicana de Matemáticas
urlname: omm
logo-title: ../assets/img/Logo-omm.png
layout: home
---

  <div class="row row-cols-1 row-cols-xl-4 row-cols-md-3 g-4">
  {% assign nacionales = site.data.nacionales_omm | sort: "year"%}
  {% for nacional in nacionales reversed%}
      <div class="col">
        <div class="card h-100 mb-3">
          <a
            href="../assets/pdf/Nacionales/OMM/{{nacional.year}}.pdf"
            target="_blank"
            rel="noopener noreferrer"
          >
            <img
              height="150px"
              style="object-fit: contain;"
              class="card-img-top border-bottom bg-white"
              src="../assets/img/{{nacional.thumbnail}}"
              alt="OMM {{ nacional.year }}">
          </a>
          <div class="card-body">
            <a
              href="../assets/pdf/Nacionales/OMM/{{nacional.year}}.pdf"
              target="_blank"
              class="card-link"
              rel="noopener noreferrer"
            >OMM {{ nacional.year }}</a>
          </div>
          <div class="card-footer">{{ nacional.location }}</div>
        </div>
      </div>
  {% endfor %}
  </div>
