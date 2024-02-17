class Text2Text:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model": ("IMAGE2TEXT_MODEL",),
                "input_string": ("STRING", {"forceInput": True}),
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

    def get_value(self, model, input_string, custom_query):
        # 由于设定了INPUT_IS_LIST = (True,)，所以所有的输入都会被转换成list
        # 所以要对参数进行预处理
        model = model[0]
        custom_query = custom_query[0]
        answers = []
        for txt in input_string:

            if model.name == "internlm":
                txt = f"{txt}"

            # Combine input text with the custom query
            combined_input = f"{txt} {custom_query}"

            result = model.answer_text_question(combined_input)
            answers.append(result)

        return (answers,)
