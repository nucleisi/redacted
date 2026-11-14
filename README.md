# [REDACTED]

> a discord bot that takes "i'm [x]" way too literally

say "i'm hungry" and it'll rename you to **hungry**. say "i am tired" and you're **tired** now. also, it'll reply with "hi [x], i'm [REDACTED]" each time (*^w^)

**[add it to your server!](<https://discord.com/oauth2/authorize?client_id=1571008674556678175&permissions=134286336&integration_type=0&scope=bot>)**

---

## what it sounds like

```
you: i'm hungry
[REDACTED]: hi hungry, i'm [REDACTED]

hungry: i am so tired
[REDACTED]: hi so tired, i'm [REDACTED]

so tired: im bored, what's for dinner
[REDACTED]: hi bored, i'm [REDACTED]
```

---

## inner workings

it matches `i'm`, `im`, `i am`, `i’m`, in any casing. whatever comes after it gets grabbed up to the first punctuation mark or the end of the message. so "im hungry, what's for dinner" only becomes **hungry**.

the regex it uses for this is written below:

```
\b(?:i['’]?m|i am)\s+(.+?)\s*(?:[.,!?;\n]|$)
```

- `i['’]?m` matches `i'm`, `im`, and `i’m`
- `i am` matches `i am`
- `(.+?)` grabs everything after it, up to the first punctuation mark or the end of the message
- it's case-insensitive, and `\b` stops it from matching inside other words

---

## stuff to know

- **role order matters!** discord won't let a bot rename anyone whose highest role is above the bot's. in server settings → roles, drag the bot's role above your members' roles if you want it to be able to rename them
- **the server owner can't be renamed** by any bot; it only works on normal members
- **nicknames max out at 32 characters**, so longer ones get trimmed before they're applied

---

## trouble?

**it's not renaming me** - check the role order (see above), and make sure you're not the server owner. also make sure it has the manage nicknames permission!

**it renamed me but didn't reply** - it needs send messages in that channel. check the channel permissions!

**it grabbed the wrong part of my message** - it stops at the first `.`, `,`, `!`, `?`, `;`, or newline. keep your "i'm [x]" at the start if you want the whole thing

---

## made with

[discord.py](https://github.com/Rapptz/discord.py)