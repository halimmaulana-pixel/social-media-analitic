# -*- coding: utf-8 -*-
"""Extract the 29 add() calls from gen_part1.py and emit one JSON per module."""
import ast, json, os, collections

SRC = "/data/data/com.termux/files/home/social-media-analytics/gen_part1.py"
OUT = "/data/data/com.termux/files/home/social-media-analytics/results"
src = open(SRC, encoding="utf-8").read()
tree = ast.parse(src)

# namespace that holds SHARED_HW / TXT_HW / ... dict definitions
ns = {}
exec(compile(src[:src.index("items = []")], "hwdefs", "exec"), ns)
HWMAP = {k: v for k, v in ns.items() if k.endswith("_HW")}

calls = [n for n in ast.walk(tree)
         if isinstance(n, ast.Call) and getattr(n.func, "id", "") == "add"]

HW = {
 "SHARED": {
  "cp": "Native platform analytics or a commercial listening dashboard (Pulsar / Talkwalker / Meltwater / Brandwatch / Sprout Social) used for read-only comparison",
  "cost": "Open-source tools are free; commercial listening seats are licensed per seat and usually out of university budget; API tiers vary per platform",
  "dc": "Define the question -> choose platform and access route -> collect via API or permitted scrape -> archive raw with checksums -> clean and document schema -> analyse -> preserve dataset and code",
  "as": "Written analysis/design document plus a short quiz; graded on correctness of concepts and quality of justification"},
 "TXT": {
  "cp": "Not the focus: commercial sentiment/topic dashboards are demonstrated read-only only for benchmarking",
  "cost": "Open-source models and data are free; GPU time (Colab/Kaggle free tier) is the practical cost; commercial NLP APIs priced per token",
  "dc": "Collect posts -> clean text -> build annotation/codebook (human + LLM) -> validate with kappa -> train/evaluate -> archive labelled data and prompts",
  "as": "Lab notebook submission plus a 1-page interpretation with error analysis; graded on correctness, interpretation and documentation"},
 "NET": {
  "cp": "Commercial trend/coordination detection tools are demonstrated only for comparison; graph work is done in open-source tools",
  "cost": "Open-source graph libraries are free; memory is the constraint for large graphs",
  "dc": "Build the interaction graph from collected data -> deduplicate accounts and edges -> compute metrics -> cluster communities -> archive graph object and code",
  "as": "Lab notebook plus graph figures and a short interpretation; graded on correctness of metrics and defensibility of substantive claims"},
 "DOM": {
  "cp": "Native creator/platform analytics (TikTok Creator Marketplace, YouTube Studio, Instagram Insights) are the primary reference; commercial tools demoed read-only",
  "cost": "Media and metric access is free via public APIs and native analytics; commercial measurement platforms are licensed to agencies",
  "dc": "Collect short-video metadata and media -> transcribe/OCR -> extract retention and engagement features -> normalise by follower base -> analyse and report",
  "as": "Lab submission plus a short strategy recommendation memo; graded on metric validity and quality of reasoning"},
 "VIZ": {
  "cp": "Tableau Public / Power BI teaching licences where available; Streamlit/Shiny as free default",
  "cost": "Open-source stack is free; some BI teaching licences are institution-dependent",
  "dc": "Collect -> clean -> aggregate per unit/time -> build dashboard -> write insight memo -> preserve data and code",
  "as": "Dashboard plus one-page insight memo, peer-reviewed against a rubric; graded on clarity, honesty and completeness"},
 "TOOL": {
  "cp": "Brandwatch / Meltwater / Talkwalker / Sprout Social / Pulsar trials or public demos for benchmark comparison",
  "cost": "Build (open source) is free; buy (commercial seat) is licensed; agent APIs are metered per call",
  "dc": "Define benchmark question -> collect once -> analyse in both stacks -> compare outputs, runtimes and costs -> document discrepancy sources",
  "as": "Benchmark report plus a build-vs-buy justification; graded on evidence quality and cost reasoning"},
 "ETH": {
  "cp": "None (ethics and governance module)",
  "cost": "None - methods and templates are free",
  "dc": "Identify data and legal basis -> DPIA/risk assessment -> collect only what is needed -> anonymise -> document retention and disclosure -> preserve the ethics note",
  "as": "Ethics/DPIA note graded with a rubric; includes defence of sampling, retention, anonymisation and disclosure choices"},
}

ETHICS_LEGAL = ("The module itself: data protection principles, consent and re-identification risk, "
 "IRB/ethics-review workflow, research reproducibility duties, algorithmic accountability "
 "(DSA/platform transparency), and consequences of violating platform Terms of Service.")

group_of = {
 "fondasi": "SHARED", "ekosistem-platform": "SHARED", "jenis-data": "SHARED",
 "akuisisi-api": "SHARED", "akuisisi-meta-fb": "SHARED", "scraping-legalitas": "SHARED",
 "preprocessing": "SHARED", "data-access-governance": "SHARED",
 "text-mining-dasar": "TXT", "sentiment-analysis": "TXT", "nlp-indonesia": "TXT",
 "topic-modeling": "TXT", "nlp-modern-llm": "TXT", "llm-as-annotator": "TXT",
 "analitik-multimodal": "TXT", "agentic-ai-social-listening": "TXT",
 "sna-dasar": "NET", "difusi-viralitas": "NET", "influence-coordinated": "NET",
 "misinformation": "NET", "synthetic-content": "NET",
 "engagement-perilaku": "DOM", "audience-profiling": "DOM",
 "short-video-analytics": "DOM", "creator-economy-commerce": "DOM",
 "visualisasi-dashboard": "VIZ", "tools-stack": "TOOL",
 "etika-legal": "ETH", "studi-kasus-capstone": "ETH",
}

UNCERTAIN = ["exact_pricing_x_api_2026", "somar_vde_fee_2026_in_idr",
             "jumlah_minggu_tepat_per_modul"]

os.makedirs(OUT, exist_ok=True)
written = []
for node in calls:
    a = []
    for x in node.args:
        if isinstance(x, ast.Name):
            a.append(HWMAP[x.id])
        else:
            a.append(ast.literal_eval(x))
    n = len(a)
    mid = a[0]
    if mid not in group_of:
        raise SystemExit("unknown item id: %s" % mid)
    hw = a[-3]
    if mid == "etika-legal":
        hw = dict(hw)
        hw["ethics_regulation"] = ETHICS_LEGAL
    g = HW[group_of[mid]]

    d = collections.OrderedDict()
    d["module_name"] = a[1]
    d["module_description"] = a[2]
    d["duration_weeks"] = a[3]
    d["core_concepts"] = a[4]
    d["learning_outcomes"] = a[5]
    d["methods_models"] = a[6]
    d["evaluation_metrics"] = a[7]
    d["pitfalls_limitations"] = a[8]
    d["tools_stack"] = a[9]

    if n == 20:
        d["commercial_platforms"] = a[10]
        d["tools_access_cost"] = a[11]
        d["lab_activities"] = a[12]
        d["datasets_apis"] = a[13]
        books, papers, trends, cap, deliver = a[14], a[15], a[16], a[18], a[19]
        d.setdefault("assessment_methods", g["as"])
    elif n == 19:
        d["lab_activities"] = a[10]
        d["datasets_apis"] = a[11]
        d["assessment_methods"] = a[12]
        books, papers, trends, cap, deliver = a[13], a[14], a[15], a[17], a[18]
        d.setdefault("commercial_platforms", g["cp"])
        d.setdefault("tools_access_cost", g["cost"])
    elif n == 18:
        d["commercial_platforms"] = a[10]
        d["tools_access_cost"] = a[11]
        d["lab_activities"] = ("Draft and defend an ethics / DPIA note for a proposed capstone "
                               "dataset; peer-reviewed against the course rubric")
        d["datasets_apis"] = ("Policy documents, platform transparency reports and Terms of "
                              "Service as a text corpus; no personal data collected")
        books, papers, trends, cap, deliver = a[12], a[13], a[14], a[16], a[17]
        d.setdefault("assessment_methods", g["as"])
    else:
        raise SystemExit("unexpected arity %d for %s" % (n, mid))

    d["data_collection_workflow"] = g["dc"]
    d["assessment_methods"] = d.get("assessment_methods") or g["as"]
    d["textbooks"] = books
    d["key_papers"] = papers
    d["trends_2024_2026"] = trends
    d["industry_relevance"] = hw["industry_relevance"]
    d["localization_context"] = hw["localization_context"]
    d["ethics_regulation"] = hw["ethics_regulation"]
    d["case_study_scenarios"] = cap
    d["deliverable_format"] = deliver
    d["uncertain"] = list(UNCERTAIN)

    path = os.path.join(OUT, mid + ".json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    written.append(path)

print("written:", len(written))
