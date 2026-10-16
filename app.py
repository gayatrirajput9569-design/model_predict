    .intro { max-width:530px; color:var(--muted); line-height:1.75; font-size:15px; }
    .hero-art { min-height:190px; padding:26px; border-radius:26px; color:white; overflow:hidden; position:relative;
      background:linear-gradient(135deg,#14284b,#315ee6 68%,#28bfc7); box-shadow:0 20px 45px #284f9b26; }
    .hero-art:after { content:""; position:absolute; width:210px; height:210px; border:1px solid #ffffff30; border-radius:50%; right:-60px; top:-72px; box-shadow:0 0 0 25px #ffffff0d,0 0 0 50px #ffffff0a; }
    .art-label { font-size:12px; text-transform:uppercase; letter-spacing:1.4px; opacity:.8; }
    .art-title { font-size:24px; font-weight:800; margin-top:15px; max-width:260px; line-height:1.2; }
    .art-bottom { display:flex; gap:8px; margin-top:23px; flex-wrap:wrap; }
    .art-chip { border:1px solid #ffffff50; background:#ffffff18; padding:7px 10px; border-radius:10px; font-size:11px; }
    .panel { background:var(--card); border:1px solid #ffffff; border-radius:24px; padding:28px; box-shadow:0 18px 55px #1c37610d; }
    .panel-head { display:flex; justify-content:space-between; align-items:flex-start; gap:16px; margin-bottom:23px; }
    h2 { margin:0 0 7px; font-size:21px; letter-spacing:-.5px; color:var(--navy); }
    .sub { margin:0; color:var(--muted); font-size:13px; line-height:1.5; }
    .grid { display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:18px; }
    label { display:block; font-size:12px; font-weight:750; margin-bottom:9px; color:#42516a; }
    input, select { width:100%; min-height:48px; padding:0 13px; border:1px solid var(--line); border-radius:12px; background:#fbfcff; color:var(--ink); font:inherit; outline:none; transition:.2s; }
    input:focus, select:focus { border-color:#6d8bff; box-shadow:0 0 0 4px #3767f516; background:white; }
    .hint { margin-top:7px; color:#8b97a9; font-size:11px; }
    .actions { display:flex; align-items:center; gap:14px; flex-wrap:wrap; margin-top:25px; }
    button { border:0; cursor:pointer; color:white; font-size:14px; font-weight:800; padding:15px 22px; border-radius:13px;
      background:linear-gradient(110deg,var(--blue),#5b78ff); box-shadow:0 9px 20px #3767f52c; transition:transform .2s, box-shadow .2s; }
    button:hover { transform:translateY(-2px); box-shadow:0 13px 25px #3767f540; }
    .safe { color:var(--muted); font-size:12px; }
    .result { margin-top:22px; border-radius:18px; padding:22px; background:linear-gradient(120deg,#edfdfb,#f0f4ff); border:1px solid #d8f2ef; }
    .result-label { color:#527083; font-size:12px; font-weight:800; text-transform:uppercase; letter-spacing:1px; }
    .amount { color:#153c6c; font-size:clamp(30px,4vw,42px); font-weight:850; letter-spacing:-1.5px; margin:8px 0; }
    .result-note { color:#60758b; font-size:12px; line-height:1.6; }
    .error { margin-top:18px; padding:13px 15px; border-radius:12px; background:#fff0f0; color:#a52828; border:1px solid #ffd5d5; font-size:13px; }
    .foot { text-align:center; color:#91a0b5; font-size:11px; margin-top:25px; line-height:1.7; }
    @media(max-width:800px) { .hero { grid-template-columns:1fr; gap:22px; } .hero-art { min-height:165px; } .grid { grid-template-columns:repeat(2,minmax(0,1fr)); } header { margin-bottom:25px; } }
    @media(max-width:520px) { .wrap { width:94%; padding-top:18px; } .pill { display:none; } .panel { padding:20px 16px; } .grid { grid-template-columns:1fr; gap:15px; } h1 { letter-spacing:-1.4px; } .panel-head { flex-direction:column; } .actions button { width:100%; } }
  </style>
</head>
<body>
  <main class="wrap">
    <header>
      <div class="brand"><div class="logo">✦</div><div>HealthCost <span style="color:#3767f5">AI</span></div></div>
      <div class="pill">● &nbsp; MACHINE LEARNING PREDICTION</div>
    </header>
    <section class="hero">
      <div>
        <div class="eyebrow">Smart prediction tool</div>
        <h1>Understand your<br><span>estimated cost.</span></h1>
        <p class="intro">Enter the details below to generate an estimated insurance charge using your trained Linear Regression model. Simple inputs, instant results.</p>
      </div>
      <div class="hero-art">
        <div class="art-label">Powered by your model</div>
        <div class="art-title">Data in.<br>Prediction out.</div>
        <div class="art-bottom"><span class="art-chip">Linear Regression</span><span class="art-chip">Flask Web App</span></div>
      </div>
    </section>
    <section class="panel">
      <div class="panel-head">
        <div><h2>Enter your details</h2><p class="sub">Complete all six fields to calculate the estimate.</p></div>
        <div class="pill">6 INPUT FEATURES</div>
      </div>
      <form method="POST" action="/">
        <div class="grid">
          <div><label for="age">Age</label><input id="age" name="age" type="number" min="18" max="100" value="{{ values.age }}" placeholder="e.g. 28" required><div class="hint">Age in years</div></div>
          <div><label for="sex">Sex</label><select id="sex" name="sex" required><option value="">Select sex</option><option value="female" {% if values.sex == 'female' %}selected{% endif %}>Female</option><option value="male" {% if values.sex == 'male' %}selected{% endif %}>Male</option></select></div>
          <div><label for="bmi">BMI</label><input id="bmi" name="bmi" type="number" min="10" max="80" step="0.1" value="{{ values.bmi }}" placeholder="e.g. 26.5" required><div class="hint">Body Mass Index</div></div>
          <div><label for="children">Number of children</label><input id="children" name="children" type="number" min="0" max="20" value="{{ values.children }}" placeholder="e.g. 1" required></div>
          <div><label for="smoker">Smoker?</label><select id="smoker" name="smoker" required><option value="">Select answer</option><option value="no" {% if values.smoker == 'no' %}selected{% endif %}>No</option><option value="yes" {% if values.smoker == 'yes' %}selected{% endif %}>Yes</option></select></div>
          <div><label for="region">Region</label><select id="region" name="region" required><option value="">Select region</option><option value="northeast" {% if values.region == 'northeast' %}selected{% endif %}>Northeast</option><option value="northwest" {% if values.region == 'northwest' %}selected{% endif %}>Northwest</option><option value="southeast" {% if values.region == 'southeast' %}selected{% endif %}>Southeast</option><option value="southwest" {% if values.region == 'southwest' %}selected{% endif %}>Southwest</option></select></div>
        </div>
        <div class="actions"><button type="submit">✦ &nbsp; Predict estimated charge</button><span class="safe">Your result appears below the form.</span></div>
      </form>
      {% if prediction is not none %}
      <div class="result" role="status">
        <div class="result-label">Estimated insurance charge</div>
        <div class="amount">{{ prediction }}</div>
        <div class="result-note">This is a model-generated estimate, not a quote or medical/financial advice. Actual charges may differ.</div>
      </div>
      {% endif %}
      {% if error %}<div class="error">{{ error }}</div>{% endif %}
    </section>
    <div class="foot">Built with Flask + scikit-learn &nbsp;•&nbsp; Predictions depend on the model and its training data.</div>
  </main>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    values = {
        "age": "", "sex": "", "bmi": "", "children": "",
        "smoker": "", "region": ""
    }
    prediction = None
    error = None

    if request.method == "POST":
        values = {key: request.form.get(key, "").strip() for key in values}
        try:
            age = int(values["age"])
            bmi = float(values["bmi"])
            children = int(values["children"])
            sex = values["sex"].lower()
            smoker = values["smoker"].lower()
            region = values["region"].lower()

            if not 18 <= age <= 100:
                raise ValueError("Please enter an age between 18 and 100.")
            if not 10 <= bmi <= 80:
                raise ValueError("Please enter a BMI between 10 and 80.")
            if not 0 <= children <= 20:
                raise ValueError("Please enter a valid number of children.")
            if sex not in SEX_MAP or smoker not in SMOKER_MAP or region not in REGION_MAP:
                raise ValueError("Please select a valid option for every field.")

            input_data = pd.DataFrame([{
                "age": age,
                "sex": SEX_MAP[sex],
                "bmi": bmi,
                "children": children,
                "smoker": SMOKER_MAP[smoker],
                "region": REGION_MAP[region],
            }], columns=FEATURES)

            result = float(model.predict(input_data)[0])
            prediction = f"${result:,.2f}"
        except (ValueError, TypeError) as exc:
            error = str(exc) or "Please check the entered values and try again."
        except Exception:
            app.logger.exception("Prediction failed")
            error = "Prediction failed. Check that the input encoding matches the model's training data."

    return render_template_string(PAGE, values=values, prediction=prediction, error=error)
