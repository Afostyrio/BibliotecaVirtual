---
title: Olimpiada Básica de Matemáticas
urlname: obmguanajuato
logo-title: ../assets/img/Logo.png
layout: home
altname: La poderosísima OBM
---

{% for edition in site.data.selectivos.obm reversed %}
<div class="row">
    <div class="col mb-3">
    <h2 class="text-center">{{edition.year}}</h2>
        <div class="row row-cols-1 row-cols-xl-4 row-cols-md-3 g-4">
        {% for exam in edition.exams %}
        {% for file in exam.files %}
          <div class="col">
              <div class="card h-100 mb-3">
                  <a
                      href="{{site.baseurl}}/assets/pdf/Selectivos/OBM/{{file.filename}}"
                      target="_blank"
                      rel="noopener noreferrer"
                  >
                      <img
                          height="150px"
                          style="object-fit: contain;"
                          class="card-img-top border-bottom bg-white"
                          src="{{site.baseurl}}/assets/img/{{edition.thumbnail}}"
                          alt="Selectivo {{ exam-number }}">
                  </a>
                  <div class="card-body">
                      <a
                          href="{{site.baseurl}}/assets/pdf/Selectivos/OBM/{{file.filename}}"
                          target="_blank"
                          class="card-link"
                          rel="noopener noreferrer"
                      >Selectivo {{ exam.number }}</a>
                      {{ edition.year }}
                  </div>
                  <div class="card-footer text-body-secondary text-end">
                      Nivel: {{ file.level }}
                  </div>
              </div>
          </div>
        {% endfor %}
        {% endfor %}
        </div>
    </div>
</div>
{% endfor %}