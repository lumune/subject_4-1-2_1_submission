# 数当てゲームプログラム
# 1〜100の間の数字をランダムに選択し、ユーザーがその数字を当てるゲーム

import random

def main():
    """数当てゲームのメイン関数"""
    # 1〜100の間のランダムな数字を生成
    target_number = random.randint(1, 100)
    
    # 試行回数をカウントする変数を初期化
    attempts = 0
    
    # ゲーム開始のメッセージを表示
    print("🎯 数当てゲーム")
    print("1〜100の間の数字を当ててください！")
    print("-" * 40)
    
    # 正解するまでループを続ける
    while True:
        try:
            # ユーザーに数字の入力を求める
            user_input = input("数字を入力してください: ")
            
            # 文字列を整数に変換（エラー処理のためにtry-except内で実行）
            guess = int(user_input)
            
            # 入力された数字が1〜100の範囲内かチェック
            if guess < 1 or guess > 100:
                print("エラー: 1〜100の間の数字を入力してください。")
                # 範囲外の場合は試行回数にカウントせず、次のループに進む
                continue
            
            # 有効な入力なので試行回数を1増やす
            attempts += 1
            
            # 入力された数字と正解を比較してヒントを表示
            if guess < target_number:
                # 入力された数字が正解より小さい場合
                print("もっと大きい")
            elif guess > target_number:
                # 入力された数字が正解より大きい場合
                print("もっと小さい")
            else:
                # 正解した場合
                print(f"🎉 正解です！答えは {target_number} でした！")
                print(f"試行回数: {attempts} 回")
                # 正解したのでループを終了
                break
                
        except ValueError:
            # 数字以外（文字列など）が入力された場合のエラー処理
            print("エラー: 数字を入力してください。")
            # 無効な入力なので試行回数にカウントせず、次のループに進む
            continue
        except Exception as e:
            # 予期しないエラーが発生した場合の処理
            print(f"エラーが発生しました: {e}")
            continue

# プログラムのエントリーポイント
# このファイルが直接実行された場合のみmain()関数を呼び出す
if __name__ == "__main__":
    main()
