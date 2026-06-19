%global debug_package %{nil}

Name:           catppuccin-cursors
Version:        2.0.0
Release:        %autorelease
Summary:        Catppuccin cursor themes

License:        GPL-3.0-or-later
URL:            https://github.com/catppuccin/cursors

BuildArch:      noarch
BuildRequires:  unzip

%global flavors \
    frappe \
    latte \
    macchiato \
    mocha

%global accents \
    blue \
    dark \
    flamingo \
    green \
    lavender \
    light \
    maroon \
    mauve \
    peach \
    pink \
    red \
    rosewater \
    sapphire \
    sky \
    teal \
    yellow

%{lua:
local source = 0
local version = rpm.expand("%{version}")

for flavor in rpm.expand("%{flavors}"):gmatch("%S+") do
    for accent in rpm.expand("%{accents}"):gmatch("%S+") do
        print(string.format(
            "Source%d: https://github.com/catppuccin/cursors/releases/download/v%s/catppuccin-%s-%s-cursors.zip\n",
            source,
            version,
            flavor,
            accent
        ))
        source = source + 1
    end
end
}

Requires:       %{name}-frappe = %{version}-%{release}
Requires:       %{name}-latte = %{version}-%{release}
Requires:       %{name}-macchiato = %{version}-%{release}
Requires:       %{name}-mocha = %{version}-%{release}

%description
Meta package for all Catppuccin cursor themes.

%package frappe
Summary:        Catppuccin Frappé cursor themes

%description frappe
Catppuccin Frappé cursor themes in all accent colors.

%package latte
Summary:        Catppuccin Latte cursor themes

%description latte
Catppuccin Latte cursor themes in all accent colors.

%package macchiato
Summary:        Catppuccin Macchiato cursor themes

%description macchiato
Catppuccin Macchiato cursor themes in all accent colors.

%package mocha
Summary:        Catppuccin Mocha cursor themes

%description mocha
Catppuccin Mocha cursor themes in all accent colors.

%prep
%setup -q -T -c

%{lua:
local source = 0

for flavor in rpm.expand("%{flavors}"):gmatch("%S+") do
    for accent in rpm.expand("%{accents}"):gmatch("%S+") do
        local dirname = string.format(
            "catppuccin-%s-%s-cursors",
            flavor,
            accent
        )

        print(string.format(
            "unzip -q %%{SOURCE%d} -d %s\n",
            source,
            dirname
        ))

        source = source + 1
    end
end
}

%install
install -d %{buildroot}%{_datadir}/icons

for dir in catppuccin-*-cursors; do
    install -d %{buildroot}%{_datadir}/icons/${dir}

    cp -a "${dir}"/* \
        %{buildroot}%{_datadir}/icons/${dir}/

    rm -f %{buildroot}%{_datadir}/icons/${dir}/LICENSE
    rm -f %{buildroot}%{_datadir}/icons/${dir}/AUTHORS
done

%files

%files frappe
%license catppuccin-frappe-blue-cursors/LICENSE
%doc catppuccin-frappe-blue-cursors/AUTHORS
%{_datadir}/icons/catppuccin-frappe-*-cursors/

%files latte
%license catppuccin-latte-blue-cursors/LICENSE
%doc catppuccin-latte-blue-cursors/AUTHORS
%{_datadir}/icons/catppuccin-latte-*-cursors/

%files macchiato
%license catppuccin-macchiato-blue-cursors/LICENSE
%doc catppuccin-macchiato-blue-cursors/AUTHORS
%{_datadir}/icons/catppuccin-macchiato-*-cursors/

%files mocha
%license catppuccin-mocha-blue-cursors/LICENSE
%doc catppuccin-mocha-blue-cursors/AUTHORS
%{_datadir}/icons/catppuccin-mocha-*-cursors/

%changelog
%autochangelog
