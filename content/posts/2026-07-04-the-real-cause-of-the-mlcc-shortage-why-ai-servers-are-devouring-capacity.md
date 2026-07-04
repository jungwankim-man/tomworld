---
title: "The Real Cause of the MLCC Shortage — Why AI Servers Are Devouring Capacity"
date: 2026-07-04T12:17:37+09:00
draft: false
categories: ["시사이슈"]
description: "\"Smartphones aren't selling, so why can't we get our hands on MLCCs?\""
tags: ["MLCC", "Shortage", "AI Servers", "Samsung Electro-Mechanics", "Murata"]
cover:
  image: "/images/posts/2026-07-04-the-real-cause-of-the-mlcc-shortage-why-ai-servers-are-devouring-capacity/real-00109.png"
  alt: "The Real Cause of the MLCC Shortage — Why AI Servers Are Devouring Capacity"
---
"Smartphones aren't selling, so why can't we get our hands on MLCCs?"

A junior colleague threw that question at me during last month's procurement meeting. At first I just answered "because of AI servers," but the deeper I dug, the more I realized this isn't a volume problem — it's a capacity problem. Statistics show AI servers consume only 2–3% of global MLCC shipments. Yet they eat up roughly 10% of capacity. That gap is the true face of this shortage.

In this post, I'll unpack the logic procurement folks can use when negotiating with suppliers, along with the background general readers need to understand terms like "20-week lead time" that keep popping up in the news.

## The Math: How AI Servers' 2% Swallows 10% of Capacity

![The Math: How AI Servers' 2% Swallows 10% of Capacity](/images/posts/2026-07-04-the-real-cause-of-the-mlcc-shortage-why-ai-servers-are-devouring-capacity/real-00109.png)

MLCCs (Multi-Layer Ceramic Capacitors) are smaller than a grain of rice. A single smartphone uses 800–1,000 of them; a standard server uses about 2,000. But a single AI server devours 15,000–28,000. Industry estimates put a single NVIDIA GB200 board at around 6,500, with next-gen Rubin climbing to 12,000.

This is where the first optical illusion kicks in. By shipment volume alone, AI servers still only account for 2–3% of total MLCC consumption. "Doesn't sound like much" — until you look at capacity.

- Yield gap: high-end MLCC yield around 40% vs. commodity 99% → you have to run the line 2.5× as much to produce the same count
- Cycle time gap: high-end 50 days vs. commodity 27 days → line turnover is less than half
- Result: converting one standard line to high-end means losing roughly four-fifths of its capacity

A line that used to pump out 100 won worth of product now yields only 20 won worth. Grasp this one piece of math and the question "AI demand is small — why is everyone out of stock?" answers itself.

> 💡 Key point: AI servers take 2–3% of MLCC volume but 10% of capacity — a gap forged by 40% yield and 50-day cycles.

## Murata, Samsung Electro-Mechanics, and Taiyo Yuden Are Ripping Up Their Lines

![Murata, Samsung Electro-Mechanics, and Taiyo Yuden Are Ripping Up Their Lines](/images/posts/2026-07-04-the-real-cause-of-the-mlcc-shortage-why-ai-servers-are-devouring-capacity/real-00110.png)

What makes this cycle different from past ones is that all three major suppliers are simultaneously converting consumer lines into AI lines. Murata's Shimane Izumo, Samsung Electro-Mechanics' Philippines site, Taiyo Yuden's Niigata — none of them come online until after 2027. With no new capacity available now, the only move is to rip up existing lines.

The problem is the 1:5 capacity loss I mentioned earlier. Convert a standard line to high-capacity, high-end production and the physical output drops to one-fifth. That's why suppliers are slashing 10–20% off existing customer allocations.

One of the set makers I handle got a notice from Murata back in May: "quarterly allocation cut by 15%." Two years ago the same rep was pushing us to buy more; now they won't even quote. Samsung Electro-Mechanics has halted distribution-channel quotes entirely, and utilization has crossed 95%.

- Murata: April hike of 15–35% → additional 10–40% hike; lead times from 8–12 weeks to 16–24 weeks
- Samsung Electro-Mechanics: utilization above 95%, distribution quotes suspended, high-end prioritized in allocation
- Taiyo Yuden: preemptive 6–13% hike in April, AI and automotive lines prioritized

The three companies look coordinated, but really it's just supply-side physics pushing them the same way.

> 💡 Key point: Converting consumer lines to AI means accepting a 4/5 capacity loss. That's why existing allocations get cut.

## Shenzhen Huaqiangbei Prices Update Every 30 Minutes

![Shenzhen Huaqiangbei Prices Update Every 30 Minutes](https://images.pexels.com/photos/30426391/pexels-photo-30426391.jpeg?auto=compress&cs=tinysrgb&h=650&w=940)

While Korea groans about "20-week lead times," China has already entered a much more severe phase. MLCC prices at Shenzhen's Huaqiangbei electronics market shift every 30 minutes. Reports show some models have doubled; the worst have jumped 20×.

Three layers explain why.

1. Self-sufficiency: China's high-end MLCC self-sufficiency is under 20%. The rest depends on Murata, Samsung Electro-Mechanics, and Taiyo Yuden.
2. Tariff and geopolitical risk: relying on Korean and Japanese supply is itself a structural stress point.
3. Hoarding: Taiwanese and Chinese distributors are stockpiling X5R commodity parts preemptively, some buying 3–6 months of supply ahead.

Distribution-side hoarding piles on top. LTA (long-term supply agreement) orders are up 120% year over year, and channel inventory has dropped to 1–1.5 months. The normal level is 2.5–3 months, but right now the entire market runs on "grab it while you can."

Honestly, my own company decided back in June to "secure three months of commodity parts up front." It turned out to be the right call, but the problem is that every procurement team in the world is making the same decision simultaneously. Hoarding worsens the shortage, which drives more hoarding — a self-reinforcing loop.

> 💡 Key point: China's sub-20% self-sufficiency + hoarding + a 120% LTA jump → Huaqiangbei prices swing in real time.

## Why Goldman Calls This "the Longest Cycle Ever"

![Why Goldman Calls This "the Longest Cycle Ever"](/images/posts/2026-07-04-the-real-cause-of-the-mlcc-shortage-why-ai-servers-are-devouring-capacity/real-00113.png)

Goldman Sachs has labeled this cycle "the largest and longest MLCC supercycle in history." Their view is that it could run through 2030. The high-end shortage, they say, will last at least until 2027–28.

Dissecting why the outlook is this bullish, a lot hinges on the fact that the triggers are stacked in H2 2026.

- Google's 8th-gen TPU enters mass production
- Amazon's 4th-gen Trainium enters mass production
- Meta's MTIA 400 and 450 enter mass production
- NVIDIA's GB300, followed by the Rubin roadmap

All that volume has to run through Murata and Samsung Electro-Mechanics lines. But the new plants in the Philippines and Izumo don't come online until 2027. The result: a structural shortage from H2 2026 through H1 2027 is locked in.

The book-to-bill ratio hitting 1.26 — a five-year high — means incoming orders are 26% larger than outgoing shipments. Until that number drops below 1.0, buyers hold the weak hand at the negotiating table.

One more optical illusion worth flagging: the AI server boom will cool eventually. But even when it does, suppliers that have already ripped up their lines will need time to revert them to commodity production. That's the structural reason this cycle has to run long.

> 💡 Key point: The H2 2026 AI-chip rush + a gap in new plants until 2027 = at least two years of structural shortage.

## Three Things Procurement Teams Need to Do Right Now

![Three Things Procurement Teams Need to Do Right Now](/images/posts/2026-07-04-the-real-cause-of-the-mlcc-shortage-why-ai-servers-are-devouring-capacity/real-00114.png)

Now that the logic is clear, let's close on the practical side. Given the character of this shortage, here are the three points procurement managers need to nail down right now.

First, identify the parts in your BOM that overlap with AI server specs. Assume high-end X7R and high-capacity parts won't free up until 2027, and pre-qualify alternate vendors (Yageo, Hong Kong–based tier 3s) now. Ours took four months just for that qualification.

Second, when signing LTAs, negotiate volume and price separately. Locking in volume today is effectively reserving capacity. For price, your best defense is a re-negotiation clause triggered by Murata's official price hike announcements. The principle: "price later, volume now."

Third, monitor channel inventory in real time. Huaqiangbei and Taiwanese distributor prices are leading indicators. Once channel inventory drops below one month, domestic lead times will spike within three. You don't need 30-minute updates, but weekly is the minimum.

The bottom line: this shortage isn't "demand went up so we're short" — it's "AI reshaped the capacity structure so we're short." Even if smartphone sales recover, the commodity lines themselves are disappearing, so the old slack won't come back.

If you're in procurement, you now have the logic to sell this to suppliers and executives. If you're an investor, I hope you've got your answer to "why is Samsung Electro-Mechanics' stock ripping." Mark the next quarter's official Murata price hike announcement on your calendar — that's the next inflection point in this cycle.

### 출처

https://biz.heraldcorp.com/article/10781816

https://biz.heraldcorp.com/article/10776297

https://www.g-enews.com/article/Global-Biz/2026/04/202604101533485268fbbec65dfb_1

https://www.finance-scope.com/article/view/scp202605170002

https://www.mt.co.kr/stock/2026/05/29/2026052910392859417

### Disclaimer

*이미지 출처: biz.heraldcorp.com, g-enews.com, finance-scope.com, mt.co.kr*
