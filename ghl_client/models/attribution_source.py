from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AttributionSource")


@_attrs_define
class AttributionSource:
    """
    Attributes:
        campaign (None | str | Unset):
        campaign_id (None | str | Unset):
        dclid (None | str | Unset):
        fb_event_id (None | str | Unset):  Example: Mozilla/5.0.
        fbc (None | str | Unset):
        fbclid (None | str | Unset):
        fbp (None | str | Unset):  Example: fb. 1.1674748390986.1171287961.
        gclid (None | str | Unset):  Example:
            CjOKCQjwnNyUBhCZARISAI9AYIFtNnIcWcYGIOQINz_ZoFI5SSLRRugSoPZoiEu27IZBY£1-MAIWmEaAo2VEALW_WCB.
        ip (None | str | Unset):  Example: 58.111.106.198.
        medium (None | str | Unset):  Example: survey.
        medium_id (None | str | Unset):  Example: FglfHAn30PRwsZVyQlKp.
        msclikid (None | str | Unset):
        referrer (None | str | Unset):  Example: https: //www.google.com.
        url (None | str | Unset):  Example: Trigger Link.
        user_agent (None | str | Unset):  Example: Mozilla/5.0.
        utm_content (None | str | Unset):
        utm_medium (None | str | Unset):
        utm_source (None | str | Unset):
    """

    campaign: None | str | Unset = UNSET
    campaign_id: None | str | Unset = UNSET
    dclid: None | str | Unset = UNSET
    fb_event_id: None | str | Unset = UNSET
    fbc: None | str | Unset = UNSET
    fbclid: None | str | Unset = UNSET
    fbp: None | str | Unset = UNSET
    gclid: None | str | Unset = UNSET
    ip: None | str | Unset = UNSET
    medium: None | str | Unset = UNSET
    medium_id: None | str | Unset = UNSET
    msclikid: None | str | Unset = UNSET
    referrer: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    user_agent: None | str | Unset = UNSET
    utm_content: None | str | Unset = UNSET
    utm_medium: None | str | Unset = UNSET
    utm_source: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        campaign: None | str | Unset
        if isinstance(self.campaign, Unset):
            campaign = UNSET
        else:
            campaign = self.campaign

        campaign_id: None | str | Unset
        if isinstance(self.campaign_id, Unset):
            campaign_id = UNSET
        else:
            campaign_id = self.campaign_id

        dclid: None | str | Unset
        if isinstance(self.dclid, Unset):
            dclid = UNSET
        else:
            dclid = self.dclid

        fb_event_id: None | str | Unset
        if isinstance(self.fb_event_id, Unset):
            fb_event_id = UNSET
        else:
            fb_event_id = self.fb_event_id

        fbc: None | str | Unset
        if isinstance(self.fbc, Unset):
            fbc = UNSET
        else:
            fbc = self.fbc

        fbclid: None | str | Unset
        if isinstance(self.fbclid, Unset):
            fbclid = UNSET
        else:
            fbclid = self.fbclid

        fbp: None | str | Unset
        if isinstance(self.fbp, Unset):
            fbp = UNSET
        else:
            fbp = self.fbp

        gclid: None | str | Unset
        if isinstance(self.gclid, Unset):
            gclid = UNSET
        else:
            gclid = self.gclid

        ip: None | str | Unset
        if isinstance(self.ip, Unset):
            ip = UNSET
        else:
            ip = self.ip

        medium: None | str | Unset
        if isinstance(self.medium, Unset):
            medium = UNSET
        else:
            medium = self.medium

        medium_id: None | str | Unset
        if isinstance(self.medium_id, Unset):
            medium_id = UNSET
        else:
            medium_id = self.medium_id

        msclikid: None | str | Unset
        if isinstance(self.msclikid, Unset):
            msclikid = UNSET
        else:
            msclikid = self.msclikid

        referrer: None | str | Unset
        if isinstance(self.referrer, Unset):
            referrer = UNSET
        else:
            referrer = self.referrer

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        user_agent: None | str | Unset
        if isinstance(self.user_agent, Unset):
            user_agent = UNSET
        else:
            user_agent = self.user_agent

        utm_content: None | str | Unset
        if isinstance(self.utm_content, Unset):
            utm_content = UNSET
        else:
            utm_content = self.utm_content

        utm_medium: None | str | Unset
        if isinstance(self.utm_medium, Unset):
            utm_medium = UNSET
        else:
            utm_medium = self.utm_medium

        utm_source: None | str | Unset
        if isinstance(self.utm_source, Unset):
            utm_source = UNSET
        else:
            utm_source = self.utm_source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if campaign is not UNSET:
            field_dict["campaign"] = campaign
        if campaign_id is not UNSET:
            field_dict["campaignId"] = campaign_id
        if dclid is not UNSET:
            field_dict["dclid"] = dclid
        if fb_event_id is not UNSET:
            field_dict["fbEventId"] = fb_event_id
        if fbc is not UNSET:
            field_dict["fbc"] = fbc
        if fbclid is not UNSET:
            field_dict["fbclid"] = fbclid
        if fbp is not UNSET:
            field_dict["fbp"] = fbp
        if gclid is not UNSET:
            field_dict["gclid"] = gclid
        if ip is not UNSET:
            field_dict["ip"] = ip
        if medium is not UNSET:
            field_dict["medium"] = medium
        if medium_id is not UNSET:
            field_dict["mediumId"] = medium_id
        if msclikid is not UNSET:
            field_dict["msclikid"] = msclikid
        if referrer is not UNSET:
            field_dict["referrer"] = referrer
        if url is not UNSET:
            field_dict["url"] = url
        if user_agent is not UNSET:
            field_dict["userAgent"] = user_agent
        if utm_content is not UNSET:
            field_dict["utmContent"] = utm_content
        if utm_medium is not UNSET:
            field_dict["utmMedium"] = utm_medium
        if utm_source is not UNSET:
            field_dict["utmSource"] = utm_source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_campaign(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        campaign = _parse_campaign(d.pop("campaign", UNSET))

        def _parse_campaign_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        campaign_id = _parse_campaign_id(d.pop("campaignId", UNSET))

        def _parse_dclid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dclid = _parse_dclid(d.pop("dclid", UNSET))

        def _parse_fb_event_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fb_event_id = _parse_fb_event_id(d.pop("fbEventId", UNSET))

        def _parse_fbc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fbc = _parse_fbc(d.pop("fbc", UNSET))

        def _parse_fbclid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fbclid = _parse_fbclid(d.pop("fbclid", UNSET))

        def _parse_fbp(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fbp = _parse_fbp(d.pop("fbp", UNSET))

        def _parse_gclid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gclid = _parse_gclid(d.pop("gclid", UNSET))

        def _parse_ip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ip = _parse_ip(d.pop("ip", UNSET))

        def _parse_medium(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        medium = _parse_medium(d.pop("medium", UNSET))

        def _parse_medium_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        medium_id = _parse_medium_id(d.pop("mediumId", UNSET))

        def _parse_msclikid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        msclikid = _parse_msclikid(d.pop("msclikid", UNSET))

        def _parse_referrer(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        referrer = _parse_referrer(d.pop("referrer", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_user_agent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_agent = _parse_user_agent(d.pop("userAgent", UNSET))

        def _parse_utm_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        utm_content = _parse_utm_content(d.pop("utmContent", UNSET))

        def _parse_utm_medium(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        utm_medium = _parse_utm_medium(d.pop("utmMedium", UNSET))

        def _parse_utm_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        utm_source = _parse_utm_source(d.pop("utmSource", UNSET))

        attribution_source = cls(
            campaign=campaign,
            campaign_id=campaign_id,
            dclid=dclid,
            fb_event_id=fb_event_id,
            fbc=fbc,
            fbclid=fbclid,
            fbp=fbp,
            gclid=gclid,
            ip=ip,
            medium=medium,
            medium_id=medium_id,
            msclikid=msclikid,
            referrer=referrer,
            url=url,
            user_agent=user_agent,
            utm_content=utm_content,
            utm_medium=utm_medium,
            utm_source=utm_source,
        )

        attribution_source.additional_properties = d
        return attribution_source

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
