require "imap4flags";
require "vnd.dovecot.execute";

setflag "\\seen";
execute :pipe "rspamd-pipe-spam";

