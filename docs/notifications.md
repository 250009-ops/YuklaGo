# Notifications and SMS

Q-4 is open: the CEO has not chosen the reminder channel. Build SMS for authentication first. Build web push as the reminder channel. Do not build a Telegram product surface. A Telegram reminder bot is out of scope until Q-4 says otherwise (spec §8, mobile review).

## SMS

Used for:

- Sign-in OTP.
- The five step-up triggers, with the reason line from `docs/auth-rbac.md`. The new-device case reuses the sign-in OTP. It does not send a second message.
- The new-device notice to the account's own phone (AC-43.2, AC-43.10). Copy: "Yangi qurilmadan kirildi · … · Siz emasmisiz?" with a link that opens S-04 and can end the session.

Not used for payment or signing.

Provider is unset (`SMS_PROVIDER=dev-log`). The dev sender writes the code to the API log on localhost only. Production must use a gateway that delivers inside Uzbekistan and a contract the operator can sign. Do not hard-code a vendor. The message body is the code and the reason. It does not include document contents, STIR, or money amounts.

Store the code as a hash. Lock for 10 minutes after 3 failures. Resend timer on S-01 is 60 seconds.

## Web push

PWA push for deadline reminders and "the desktop step is ready". iOS delivers web push only to a home-screen install on iOS 16.4 or later. The UI says so. Do not promise push inside a browser tab on iOS.

The worker sends from `NotificationDelivery` templates. Parameters are shipment public id and a date. Not a name and not a document snippet.

## In-app

S-04 banner on other sessions, caution colours, dismissible, action "Sessiyani tugatish".

Deadline chips on the shipment header are not notifications. They are part of the shipment read model. Customs processing times (3 h / 8 h / 1 working day) are never a countdown. The label is "bojxona ishlov muddati" (AC-8.3).

## Quiet hours

`NotificationPreference.quietHours` is optional. Default is no quiet hours. Reminders still respect it when set. OTP and step-up SMS do not. They are part of the action the user just took.
