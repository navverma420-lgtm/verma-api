@app.route("/ai/ask", methods=["GET"])
def ask_ai():

    question = request.args.get("question")

    key = request.args.get("AIzaSyD3a-9AfrSFXpPHYFQBkT3xcxYLKIjxWP8")

    if not question:
        return jsonify({
            "reply": "Question missing"
        })

    try:

        response = model.generate_content(
            question
        )

        answer = response.text

    except Exception as e:

        answer = str(e)

    return jsonify({
        "reply": answer
    })
