# AI 反方實驗室 v0.1
# 功能：點子分析、失敗模擬、使用者反駁、重新評估
# 目前為規則式原型，尚未連接真正的 AI API

def line():
    print("=" * 55)


def get_idea():
    line()
    print("       AI 反方實驗室 | IDEA CRASH TEST")
    line()
    print("輸入你的創意，讓我們測試它能不能活下來！\n")
    return input("請輸入你的點子：").strip()


def analyze_idea(idea):
    print("\n[第一階段] 找出點子的關鍵風險")
    line()

    risks = [
        {
            "name": "需求風險",
            "question": "真的有人需要這個產品嗎？",
            "test": "找 5 位目標使用者，詢問他們目前怎麼解決這個問題。"
        },
        {
            "name": "執行風險",
            "question": "你目前的時間、技術和資源足夠嗎？",
            "test": "先做一個只有核心功能的最小可行版本。"
        },
        {
            "name": "競爭風險",
            "question": "如果別人也能做出相同功能，你的優勢是什麼？",
            "test": "列出 3 個替代方案，找出你的產品真正不同的地方。"
        }
    ]

    for i, risk in enumerate(risks, 1):
        print(f"\n風險 {i}：{risk['name']}")
        print(f"反方質疑：{risk['question']}")
        print(f"驗證方式：{risk['test']}")

    return risks


def simulate_failures(idea):
    print("\n\n[第二階段] 平行世界：如果你的點子失敗了")
    line()

    worlds = [
        ("世界 A｜沒人買單",
         "大家說這個點子很棒，卻沒有人真的願意使用。"),
        ("世界 B｜強敵出現",
         "大型公司推出類似產品，而且免費提供。"),
        ("世界 C｜資源耗盡",
         "開發時間只剩原本的一半，你必須刪除部分功能。")
    ]

    for name, result in worlds:
        print(f"\n{name}")
        print(f"假想結果：{result}")
        answer = input("你會如何挽救這個點子？（輸入你的想法）：")
        print(f"你的策略：{answer if answer.strip() else '尚未提出解決方案'}")


def challenge_ai():
    print("\n\n[第三階段] 反方也要接受審判")
    line()
    print("現在換你挑戰 AI 的反對意見！")
    print("你可以提出證據、反例，或補充原本沒有的條件。\n")

    objection = input("你認為 AI 哪裡說錯了？")
    evidence = input("你有什麼證據或理由支持自己？")

    print("\n[第四階段] 重新評估")
    line()

    if not objection.strip() or not evidence.strip():
        print("資料不足，暫時無法重新評估。")
        print("請補充反駁內容與支持理由。")
        return

    print("\n收到你的反駁：")
    print(f"反駁內容：{objection}")
    print(f"支持理由：{evidence}")

    print("\n反方的暫時裁決：")
    print("你的說法提供了新的判斷材料，但還不能直接證明"
          "原本的風險已經消失。")
    print("建議：把你的理由轉換成可以實際驗證的測試。")
    print("注意：目前這是示範規則，不是真正的 AI 推理。")


def final_report(idea):
    line()
    print("                 測試報告")
    line()
    print(f"測試點子：{idea}")
    print("\n目前結果：尚未驗證")
    print("下一步：選出最重要的一項風險，收集真實證據。")
    print("提醒：被反駁不代表點子很差，沒有被反駁也不代表一定成功。")
    line()


def main():
    idea = get_idea()

    if not idea:
        print("你還沒有輸入點子，請重新執行程式。")
        return

    analyze_idea(idea)
    simulate_failures(idea)
    challenge_ai()
    final_report(idea)


if __name__ == "__main__":
    main()