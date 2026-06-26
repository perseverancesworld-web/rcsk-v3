class Dream:
    def compress(self, memory):
        top = memory.get_top_salient(5)
        return {
            "summary": [e.intent for e in top],
            "patterns": ["Recurring planning patterns detected"]
        }
