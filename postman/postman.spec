%global debug_package %{nil}
%global __strip /bin/true
%global __brp_check_rpaths %{nil}

Name:           postman
Version:        12.18.1
Release:        1%{?dist}
Summary:        Postman API Platform

License:        LicenseRef-Postman-EULA
URL:            https://www.postman.com/

Source0:        https://dl.pstmn.io/download/version/%{version}/linux64
Source1:        postman.desktop

ExclusiveArch:  x86_64

BuildRequires:  desktop-file-utils

Requires:       alsa-lib
Requires:       gtk3
Requires:       libXScrnSaver
Requires:       libXtst
Requires:       nss

%description
Postman is an API platform for building and using APIs.

%prep
%autosetup -n Postman

%build

%install
install -d %{buildroot}/opt/postman
cp -a . %{buildroot}/opt/postman/

install -d %{buildroot}%{_bindir}
ln -sf ../../opt/postman/Postman \
    %{buildroot}%{_bindir}/postman

desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications \
    %{SOURCE1}

install -Dm0644 \
    app/resources/app/assets/icon.png \
    %{buildroot}%{_datadir}/pixmaps/postman.png

%check
desktop-file-validate \
    %{buildroot}%{_datadir}/applications/postman.desktop

%files
/opt/postman
%{_bindir}/postman
%{_datadir}/applications/postman.desktop
%{_datadir}/pixmaps/postman.png

%changelog
%autochangelog