import openai
openai.api_key = "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"
def askChatGPT(question):
    prompt = question
    model_engine = "text-davinci-003"

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    print(message)
question = "简历所有词条为：['RESUME》', '》鱼洪振霞', '随时准备上岗', '求职目标:市场总监-专注品牌方向', '国出生:2001.05', '电话,，请在前面的文字中分析求职者的信息，并给他岗位建议"
askChatGPT(question)
