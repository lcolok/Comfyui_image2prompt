class Text2Text:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model": ("IMAGE2TEXT_MODEL",),
                "query": (
                    [
                        "Describe this photograph.",
                        "What is this?",
                        "Please describe this image in detail.",
                    ],
                    {
                        "default": "What is this?",
                        "multiline": True,
                    },
                ),
                "custom_query": (
                    "STRING",
                    {
                        "default": "",
                        "multiline": True,
                    },
                ),
            }
        }

    INPUT_IS_LIST = (True,)
    OUTPUT_IS_LIST = (True,)
    RETURN_TYPES = ("STRING",)
    FUNCTION = "get_value"
    CATEGORY = "fofo"

    def get_value(self, model, query, custom_query):
        # 由于设定了INPUT_IS_LIST = (True,)，所以所有的输入都会被转换成list
        # 所以要对model进行预处理
        model = model[0]
        if len(custom_query) > 0:
            query = custom_query
        answers = []
        for txt in query:

            if model.name == "internlm":
                txt = f"<ImageHere>{txt}"

            result = model.answer_text_question(txt)
            answers.append(result)

        return (answers,)
