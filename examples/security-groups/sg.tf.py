from ipaddress import IPv4Network

from pretf.api import tf


def terraform(var):

    private_label = "private"
    private = yield tf(
        f"resource.aws_security_group.{private_label}",
        {"name": "pretf-security-groups-private"},
    )

    public_label = "public"
    public = yield tf(
        f"resource.aws_security_group.{public_label}",
        {"name": "pretf-security-groups-public"},
    )

    for cidr in sorted(set(var.access_list)):

        cidr_name = cidr.replace(".", "_").replace("/", "_")

        if IPv4Network(cidr).is_global:
            group = public
            group_label = public_label
        else:
            group = private
            group_label = private_label

        for port in (80, 443):
            rule_name = f"{group_label}_{port}_from_{cidr_name}"
            yield tf(
                f"resource.aws_security_group_rule.{rule_name}",
                {
                    "security_group_id": group.id,
                    "type": "ingress",
                    "protocol": "tcp",
                    "from_port": port,
                    "to_port": port,
                    "cidr_blocks": [cidr],
                },
            )