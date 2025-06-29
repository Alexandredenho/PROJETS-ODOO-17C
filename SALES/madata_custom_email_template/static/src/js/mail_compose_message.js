/** @odoo-module **/

import { MailComposerFormController } from "@mail/views/mail_composer_form";
import { patch } from "@web/core/utils/patch";
console.log("madata_custom_email_template");
patch(MailComposerFormController.prototype, {
    setup() {
        super.setup();
        const dialogData = this.env.dialogData;
        if (dialogData) {
            dialogData.title = "Madata";
        }
    }
});