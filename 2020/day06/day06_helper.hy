(defn solver [groups func]
    (->> groups
        (map (fn [group]
            (->> (.split group)
                 (filter (fn [item] item))
                 (map (fn [item] (set item)))
                 (reduce func)
                 (len))))
        (sum)))
