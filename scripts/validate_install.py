import minedojo


if __name__ == "__main__":
    env = minedojo.make(
        task_id="combat_spider_plains_leather_armors_diamond_sword_shield",
        image_size=(288, 512),
        world_seed=123,
        seed=42,
    )

    print(f"[INFO] Create a task with prompt: {env.task_prompt}")

    env.reset()
    print(f"[INFO] reset env successfully.")
    for _ in range(20):
        obs, reward, done, info = env.step(env.action_space.no_op())
        print(f"[INFO] Step reward: {reward}, done: {done}")
    env.close()

    print("[INFO] Installation Success")
