@app.post("/save")
def save(data: dict):

    run_query("""
    INSERT INTO deals (purchase, arv, profit, transformation_cost, strategy, risk_level)
    VALUES (%s,%s,%s,%s,%s,%s)
    """, (
        data.get("purchase",0),
        data.get("arv",0),
        data.get("profit",0),
        data.get("transformation",0),
        data.get("strategy",""),
        "AUTO"
    ))

    return {"status": "saved"}
